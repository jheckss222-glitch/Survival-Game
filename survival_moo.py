#!/usr/bin/env python3
"""Campfire Cantos: a text survival game with light fantasy vibes."""

from __future__ import annotations

import json
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Dict, List

from world_data import WEATHER_DATA, WORLD_DATA


@dataclass
class WaterSource:
    """Describes a single place where the player can drink water."""

    name: str
    quality: str
    description: str


@dataclass
class Poi:
    """Describes a point of interest in an environment."""

    name: str
    description: str


@dataclass
class ResourceNode:
    """Tracks local gatherable resources with depletion, stress, and regeneration behavior."""

    item: str
    count: int
    max_count: int
    regen_rate: int
    stress: int = 0

    def harvest(self, amount: int) -> int:
        """Take up to `amount` resources from the node and return actual harvested quantity."""
        taken = min(self.count, amount)
        self.count -= taken
        return taken


@dataclass
class Environment:
    name: str
    terrain: str
    flavor: str
    gatherables: List[str]
    huntables: List[str]
    water_sources: List[WaterSource]
    pois: List[Poi]
    temp_bias: int
    resource_nodes: Dict[str, ResourceNode]
    soundscape: Dict[str, List[str]]


@dataclass
class Weather:
    name: str
    temperature_shift: int
    thirst_rate: int
    fire_modifier: float
    hunt_modifier: float
    mood: str


@dataclass
class Season:
    """Defines macro-scale climate pressure that cycles over long play windows."""

    name: str
    temp_shift: int
    regen_modifier: int
    hunt_modifier: float
    description: str


@dataclass
class Event:
    """Temporary world condition that stacks with weather and season effects."""

    name: str
    duration_hours: int
    temp_shift: int
    thirst_rate: int
    fire_modifier: float
    hunt_modifier: float
    regen_modifier: int
    description: str


@dataclass
class Shelter:
    level: int = 0
    material: str = "none"

    @property
    def label(self) -> str:
        return ["No shelter", "Lean-to", "Wattle hut", "Enchanted cabin"][self.level]


@dataclass
class Player:
    health: int = 100
    hunger: int = 25
    thirst: int = 25
    body_temp: int = 37
    location: int = 0
    hours: int = 8
    inventory: Dict[str, int] = field(default_factory=lambda: {
        "stick": 1,
        "stone": 1,
        "fiber": 0,
        "berries": 0,
        "raw_meat": 0,
        "cooked_meat": 0,
        "mushroom": 0,
        "spark_crystal": 0,
        "hide": 0,
        "rope": 0,
    })
    shelter: Shelter = field(default_factory=Shelter)
    fire_lit: bool = False
    camp_comfort: int = 0


class SurvivalGame:
    """Main game object that owns world state and executes command actions."""

    def __init__(self) -> None:
        self.world = self._load_world_from_data(WORLD_DATA)
        self.weather_types = self._load_weather_from_data(WEATHER_DATA)
        self.seasons = self._build_seasons()
        self.player = Player(location=random.randint(0, len(self.world) - 1))
        self.weather = random.choice(self.weather_types)
        self.season_length_hours = 48
        self.season_index = 0
        self.season_timer = 0
        self.current_season = self.seasons[self.season_index]
        self.active_event: Event | None = None
        self.event_timer = 0
        self.event_check_timer = 0
        self.running = True
        self.commands = self._build_command_table()

    def _load_world_from_data(self, world_data: List[dict]) -> List[Environment]:
        """Build runtime environments from data definitions to improve maintainability."""
        world: List[Environment] = []
        for entry in world_data:
            world.append(
                Environment(
                    name=entry["name"],
                    terrain=entry["terrain"],
                    flavor=entry["flavor"],
                    gatherables=entry["gatherables"],
                    huntables=entry["huntables"],
                    water_sources=[WaterSource(**w) for w in entry["water_sources"]],
                    pois=[Poi(**p) for p in entry["pois"]],
                    temp_bias=entry["temp_bias"],
                    resource_nodes={
                        item: ResourceNode(
                            item=item,
                            count=node["count"],
                            max_count=node["max"],
                            regen_rate=node["regen"],
                            stress=node.get("stress", 0),
                        )
                        for item, node in entry["resource_nodes"].items()
                    },
                    soundscape=entry.get("soundscape", {}),
                )
            )
        return world

    def _load_weather_from_data(self, weather_data: List[dict]) -> List[Weather]:
        """Build Weather objects from data definitions."""
        return [Weather(**entry) for entry in weather_data]

    def _build_seasons(self) -> List[Season]:
        """Create ordered season cycle for long-horizon survival pressure."""
        return [
            Season("Spring", 0, 1, 0.0, "Meltwater rises and growth returns; supplies recover quickly."),
            Season("Summer", 3, 0, 0.0, "Long dry days increase heat pressure and water demand."),
            Season("Autumn", -1, 0, 0.05, "Cooler air and active game trails reward preparation."),
            Season("Winter", -5, -1, -0.10, "Hard cold slows recovery and punishes poor stockpiles."),
        ]

    def _build_events(self) -> List[Event]:
        """Define low-frequency dynamic events that briefly reshape local conditions."""
        return [
            Event("Cold Snap", 18, -3, 0, 0.05, -0.05, -1, "A sharp cold front settles in and hardens surfaces."),
            Event("Clear Night", 14, -1, -1, 0.1, 0.05, 0, "Skies clear after dusk, boosting visibility and dry fuel."),
            Event("Animal Trail", 16, 0, 0, 0.0, 0.15, 0, "Fresh tracks cluster around passes and water edges."),
            Event("Midge Bloom", 12, 1, 1, -0.05, -0.05, 0, "Dense insects rise from still water and open mud."),
            Event("Berry Flush", 16, 0, 0, 0.0, 0.0, 1, "New berry growth appears along sunny margins."),
            Event("Mineral Runoff", 20, -1, 0, -0.05, 0.0, -1, "Runoff clouds channels with suspended mineral fines."),
        ]

    def _build_command_table(self) -> Dict[str, Callable[[str], None]]:
        """Map command names to handlers for clean and extensible command dispatch."""
        return {
            "help": lambda _: self.help(),
            "look": lambda _: self.describe_location(),
            "status": lambda _: self.status(),
            "inventory": lambda _: self.inventory(),
            "gather": lambda _: self.gather(),
            "hunt": lambda _: self.hunt(),
            "drink": lambda _: self.drink(),
            "eat": lambda _: self.eat(),
            "cook": lambda _: self.cook(),
            "travel": lambda _: self.travel(),
            "rest": lambda _: self.rest(),
            "extinguish": lambda _: self.extinguish(),
            "save": lambda args: self.save_game(args or "savegame.json"),
            "load": lambda args: self.load_game(args or "savegame.json"),
            "craft": self._handle_craft,
            "quit": lambda _: self._quit(),
        }

    def _quit(self) -> None:
        print("You leave the wilderness with stories and at least one mysterious rash.")
        self.running = False

    def _handle_craft(self, args: str) -> None:
        if not args:
            print("Usage: craft <item>")
            return
        self.craft(args)

    def execute_command(self, raw: str) -> None:
        """Parse and route commands through a dispatch table instead of if/elif chains."""
        command, _, args = raw.partition(" ")
        handler = self.commands.get(command)
        if handler is None:
            print("Unknown command. Type 'help' for options.")
            return
        handler(args.strip())

    def current_env(self) -> Environment:
        return self.world[self.player.location]

    def describe_location(self) -> None:
        env = self.current_env()
        print(f"\n== {env.name} ==")
        print(f"Terrain: {env.terrain}")
        print(f"Season: {self.current_season.name} ({self.season_timer}/{self.season_length_hours}h)")
        print(f"Season Note: {self.current_season.description}")

        flavor_parts = [part.strip() for part in env.flavor.split("|") if part.strip()]
        scene_setter = flavor_parts[0] if flavor_parts else env.flavor
        terrain_cover = flavor_parts[1] if len(flavor_parts) > 1 else ""
        ground_travel = flavor_parts[2] if len(flavor_parts) > 2 else ""
        air_light = flavor_parts[3] if len(flavor_parts) > 3 else ""

        print(f"\n{scene_setter}")
        if terrain_cover:
            print(f"\nTerrain & Cover: {terrain_cover}")
        if ground_travel:
            print(f"Ground & Travel: {ground_travel}")
        if air_light:
            print(f"Air & Light: {air_light}")

        print(f"\nWeather — {self.weather.name}: {self.weather.mood}")
        if self.active_event:
            print(f"Active Event — {self.active_event.name}: {self.active_event.description}")

        print("\nWater:")
        for w in env.water_sources:
            print(f" - {w.name} ({w.quality}): {w.description}")

        print("\nPoints of Interest:")
        for p in env.pois:
            print(f" - {p.name}: {p.description}")

        notes: List[str] = []
        if env.temp_bias <= -5:
            notes.append("Exposure risk increases quickly if you are wet or inactive.")
        elif env.temp_bias >= 3:
            notes.append("Heat stress risk rises at midday; shade and pace matter.")

        if self.weather.name in {"Rain", "Storm"}:
            notes.append("Fire is harder to maintain in current conditions.")
        elif self.weather.name == "Frostwind":
            notes.append("Wind chill can outpace clothing insulation.")

        if notes:
            print("\nNotes:")
            for note in notes[:2]:
                print(f" - {note}")

    def status(self) -> None:
        p = self.player
        print(
            f"\nHealth:{p.health} Hunger:{p.hunger}/100 Thirst:{p.thirst}/100 "
            f"BodyTemp:{p.body_temp}C Time:{p.hours:02d}:00"
        )
        print(
            f"Shelter: {p.shelter.label} | Fire: {'lit' if p.fire_lit else 'out'} | "
            f"Season: {self.current_season.name}"
        )
        if self.active_event:
            print(f"Event: {self.active_event.name} ({self.event_timer}h left)")

        tier = "Cold Camp" if p.camp_comfort <= 2 else "Settled Camp" if p.camp_comfort <= 6 else "Cozy Camp"
        print(f"Camp Comfort: {p.camp_comfort}/10 ({tier})")
        for msg in self._stat_feedback():
            print(f" - {msg}")

    def _stat_feedback(self) -> List[str]:
        """Return threshold-based survival feedback for hunger/thirst/temperature."""
        p = self.player
        feedback: List[str] = []
        if p.hunger >= 80:
            feedback.append("Your stomach is painfully empty.")
        elif p.hunger >= 60:
            feedback.append("You are hungry.")

        if p.thirst >= 80:
            feedback.append("Your mouth is desert dry.")
        elif p.thirst >= 60:
            feedback.append("You are thirsty.")

        if p.body_temp <= 35:
            feedback.append("You are chilled and shivering.")
        elif p.body_temp >= 39:
            feedback.append("You feel overheated.")

        return feedback

    def inventory(self) -> None:
        print("\nInventory:")
        for item, count in sorted(self.player.inventory.items()):
            if count > 0:
                print(f" - {item}: {count}")

    def _event_modifier(self, attr: str, default: float = 0.0) -> float:
        if self.active_event is None:
            return default
        return float(getattr(self.active_event, attr))

    def _seasonal_regen_amount(self, node: ResourceNode, env: Environment) -> int:
        """Return per-hour regeneration under season/event pressure and local stress."""
        regen = node.regen_rate + self.current_season.regen_modifier + int(self._event_modifier("regen_modifier", 0))
        regen -= node.stress // 3

        if self.player.location == self.world.index(env) and self.player.camp_comfort >= 7:
            regen += 1

        return max(0, regen)

    def _regenerate_world_resources(self, hrs: int) -> None:
        """Regenerate resources in all environments per hour to keep exploration valuable."""
        for _ in range(hrs):
            for env in self.world:
                for node in env.resource_nodes.values():
                    regen_amount = self._seasonal_regen_amount(node, env)
                    node.count = min(node.max_count, node.count + regen_amount)

    def _reduce_node_stress(self, amount: int = 1) -> None:
        """Gradually recover stressed resource nodes over time."""
        for env in self.world:
            for node in env.resource_nodes.values():
                node.stress = max(0, node.stress - amount)

    def _advance_season_clock(self, hrs: int) -> None:
        """Rotate seasons after fixed in-game hour windows and ease over-harvest stress."""
        self.season_timer += hrs
        while self.season_timer >= self.season_length_hours:
            self.season_timer -= self.season_length_hours
            self.season_index = (self.season_index + 1) % len(self.seasons)
            self.current_season = self.seasons[self.season_index]
            self._reduce_node_stress(1)
            print(f"\nSeason shift! {self.current_season.name} settles over the land.")

    def _update_event_clock(self, hrs: int) -> None:
        """Advance active events and roll for rare new events every 24 hours."""
        if self.active_event:
            self.event_timer -= hrs
            if self.event_timer <= 0:
                print(f"\nEvent fades: {self.active_event.name} passes.")
                self.active_event = None
                self.event_timer = 0

        self.event_check_timer += hrs
        while self.event_check_timer >= 24:
            self.event_check_timer -= 24
            if self.active_event is None and random.random() < 0.10:
                options = self._build_events()
                if self.current_season.name == "Winter":
                    options.append(Event("Cold Snap", 20, -3, 0, 0.05, -0.05, -1, "A sharp cold front settles in and hardens surfaces."))
                self.active_event = random.choice(options)
                self.event_timer = self.active_event.duration_hours
                print(f"\nEvent begins: {self.active_event.name}. {self.active_event.description}")

    def _update_camp_comfort(self, hrs: int) -> None:
        """Track earned camp comfort from sustained fire and shelter stability."""
        p = self.player
        if p.fire_lit:
            p.camp_comfort = min(10, p.camp_comfort + hrs)
        else:
            decay = hrs
            if p.shelter.level > 0:
                decay = max(0, decay - 1)
            p.camp_comfort = max(0, p.camp_comfort - decay)

    def _update_fire_from_weather(self) -> None:
        """Weather/event can extinguish fire; established camps resist better."""
        if not self.player.fire_lit:
            return

        fire_mod = self.weather.fire_modifier + self._event_modifier("fire_modifier", 0.0)
        failure_chance = max(0.0, 0.12 - fire_mod)
        if self.player.camp_comfort >= 6:
            failure_chance = max(0.0, failure_chance - 0.04)

        if random.random() < failure_chance:
            self.player.fire_lit = False
            print("A wet gust strips heat from the coals and the ember bed collapses to a dull red.")

    def _maybe_print_ambient(self, hrs: int) -> None:
        """Occasionally print lightweight biome ambience based on time, weather, and season."""
        checks = max(1, hrs // 3)
        if random.random() > (0.20 * checks):
            return

        env = self.current_env()
        mode = "day" if 6 <= self.player.hours < 19 else "night"
        if self.current_season.name == "Winter" and env.soundscape.get("winter"):
            mode = "winter"
        if self.weather.name == "Storm" and env.soundscape.get("storm"):
            mode = "storm"

        lines = env.soundscape.get(mode) or env.soundscape.get("day") or []
        if lines:
            print(f"Ambient: {random.choice(lines)}")

    def advance_time(self, hrs: int = 1) -> None:
        p = self.player
        env = self.current_env()
        p.hours = (p.hours + hrs) % 24
        self._advance_season_clock(hrs)
        self._update_event_clock(hrs)
        self._update_camp_comfort(hrs)

        if random.random() < 0.35:
            self.weather = random.choice(self.weather_types)
            print(f"\nWeather shift! It is now {self.weather.name.lower()}.")

        total_thirst_rate = self.weather.thirst_rate + int(self._event_modifier("thirst_rate", 0))

        # Balanced baseline progression: hunger rises more slowly than thirst.
        p.hunger = min(100, p.hunger + (2 + max(0, total_thirst_rate // 2)) * hrs)
        p.thirst = min(100, p.thirst + (3 + total_thirst_rate) * hrs)

        ambient_temp = (
            37
            + env.temp_bias
            + self.weather.temperature_shift
            + self.current_season.temp_shift
            + int(self._event_modifier("temp_shift", 0))
        )

        if p.fire_lit:
            p.body_temp += 1
        else:
            if ambient_temp < 34:
                p.body_temp -= 1
            elif ambient_temp > 40:
                p.body_temp += 1

        if p.shelter.level > 0:
            p.body_temp += 1 if ambient_temp < 35 else -1 if ambient_temp > 39 else 0

        self._update_fire_from_weather()
        self._regenerate_world_resources(hrs)
        if p.hours == 0:
            self._reduce_node_stress(1)
        self._maybe_print_ambient(hrs)
        self.resolve_survival()

    def resolve_survival(self) -> None:
        p = self.player
        if p.hunger >= 90:
            p.health -= 2
            print("You are starving. Your stomach grumbles in a low, hollow cadence.")
        if p.thirst >= 90:
            p.health -= 3
            print("You are dangerously dehydrated. Your mouth is dry and your tongue sits thick against your palate.")
        if p.body_temp <= 34:
            p.health -= 5
            print("Hypothermia risk! Shivering intensifies and fine motor control begins to fade.")
        if p.body_temp >= 40:
            p.health -= 5
            print("Hyperthermia risk! Heat stress builds and concentration becomes difficult.")

        p.body_temp = max(30, min(42, p.body_temp))
        if p.health <= 0:
            print("\nYou collapse from cumulative exposure and dehydration.")
            self.running = False

    def gather(self) -> None:
        env = self.current_env()
        available_nodes = [n for n in env.resource_nodes.values() if n.count > 0]
        if not available_nodes:
            print("Local resources are picked clean. Maybe travel and return later.")
            self.advance_time()
            return

        node = random.choice(available_nodes)
        requested = random.randint(1, 3)
        gathered = node.harvest(requested)
        self.player.inventory[node.item] += gathered
        print(f"You gather {gathered} x {node.item} from the {env.terrain.lower()}.")

        if node.count == 0:
            node.stress = min(10, node.stress + 1)
            print(f"The nearby {node.item} patch is temporarily depleted and shows little recent regrowth.")
        if node.stress >= 6:
            print("The patch looks thin from repeated harvesting and recovery is visibly slow.")

        self.advance_time()

    def hunt(self) -> None:
        env = self.current_env()
        target = random.choice(env.huntables)
        has_rope = self.player.inventory.get("rope", 0) > 0
        base_success = 0.45 + (0.15 if has_rope else 0)
        success = max(
            0.1,
            min(
                0.9,
                base_success
                + self.weather.hunt_modifier
                + self.current_season.hunt_modifier
                + self._event_modifier("hunt_modifier", 0.0),
            ),
        )
        if random.random() < success:
            meat = random.randint(1, 3)
            hide = random.randint(0, 2)
            self.player.inventory["raw_meat"] += meat
            self.player.inventory["hide"] += hide
            print(f"Successful hunt: {target}. You recover {meat} raw meat and {hide} hide.")
        else:
            print(f"The {target} breaks cover and escapes in the current {self.weather.name.lower()} conditions.")
        self.advance_time(2)

    def drink(self) -> None:
        env = self.current_env()
        source = random.choice(env.water_sources)
        print(f"You drink from {source.name}.")
        if source.quality in {"murky", "muddy", "risky", "salty"} and random.random() < 0.25:
            self.player.health -= 5
            print("The water quality was poor; nausea and cramping set in.")
        self.player.thirst = max(0, self.player.thirst - 35)
        self.advance_time(1)

    def craft(self, item: str) -> None:
        inv = self.player.inventory
        recipes = {
            "rope": {"fiber": 3},
            "spark_crystal": {"stone": 2},
            "campfire": {"stick": 3, "stone": 2},
            "lean-to": {"stick": 5, "fiber": 4},
            "hut": {"stick": 8, "fiber": 6, "hide": 2},
        }
        if item not in recipes:
            print("Unknown craft. Try: rope, spark_crystal, campfire, lean-to, hut")
            return

        need = recipes[item]
        if any(inv.get(k, 0) < v for k, v in need.items()):
            print(f"Missing materials for {item}: {need}")
            return

        for k, v in need.items():
            inv[k] -= v

        if item == "campfire":
            self.player.fire_lit = True
            print("You build a campfire and establish a stable heat source.")
        elif item == "lean-to":
            self.player.shelter.level = max(self.player.shelter.level, 1)
            self.player.shelter.material = "wood"
            print("You build a lean-to shelter.")
        elif item == "hut":
            self.player.shelter.level = max(self.player.shelter.level, 2)
            self.player.shelter.material = "hide & wood"
            print("You reinforce your camp into a sturdy hut.")
        else:
            inv[item] = inv.get(item, 0) + 1
            print(f"You craft {item}.")

        self.advance_time(1)

    def cook(self) -> None:
        inv = self.player.inventory
        if not self.player.fire_lit:
            print("You need a lit campfire to cook.")
            return
        if inv["raw_meat"] <= 0 and inv["mushroom"] <= 0:
            print("Nothing to cook right now.")
            return

        cooked = min(inv["raw_meat"], random.randint(1, 2))
        inv["raw_meat"] -= cooked
        inv["cooked_meat"] += cooked
        if inv["mushroom"] > 0 and random.random() < 0.5:
            inv["mushroom"] -= 1
            print("You roast a mushroom cap; the aroma is earthy and clean.")
        print(f"You cook {cooked} meat over the fire.")
        self.advance_time(1)

    def eat(self) -> None:
        inv = self.player.inventory
        if inv["cooked_meat"] > 0:
            inv["cooked_meat"] -= 1
            self.player.hunger = max(0, self.player.hunger - 35)
            print("You eat cooked meat and feel your energy return.")
        elif inv["berries"] > 0:
            inv["berries"] -= 1
            self.player.hunger = max(0, self.player.hunger - 15)
            print("You snack on berries.")
        elif inv["mushroom"] > 0:
            inv["mushroom"] -= 1
            self.player.hunger = max(0, self.player.hunger - 10)
            print("You eat a mushroom with caution and monitor for any adverse effects.")
        else:
            print("You have nothing edible right now.")
            return
        self.advance_time(1)

    def rest(self) -> None:
        heal = 8 + (4 * self.player.shelter.level)
        if self.player.fire_lit:
            heal += 4
        heal += self.player.camp_comfort // 3
        self.player.health = min(100, self.player.health + heal)
        print(f"You rest in shelter and recover {heal} health.")
        self.advance_time(3)

    def travel(self) -> None:
        old = self.current_env().name
        choices = [i for i in range(len(self.world)) if i != self.player.location]
        self.player.location = random.choice(choices)
        print(f"You travel from {old} to {self.current_env().name}.")
        self.describe_location()
        self.advance_time(2)

    def extinguish(self) -> None:
        if self.player.fire_lit:
            self.player.fire_lit = False
            print("You extinguish the campfire and save some fuel for later.")
            self.advance_time(1)
        else:
            print("Your fire is already out.")

    def save_game(self, filename: str) -> None:
        """Serialize player and world progression (including resource depletion) to JSON."""
        save_path = Path(filename)
        payload = {
            "player": {
                **asdict(self.player),
                "shelter": asdict(self.player.shelter),
            },
            "weather": asdict(self.weather),
            "season": {
                "index": self.season_index,
                "timer": self.season_timer,
            },
            "event": {
                "active": asdict(self.active_event) if self.active_event else None,
                "timer": self.event_timer,
                "check_timer": self.event_check_timer,
            },
            "world_nodes": [
                {item: asdict(node) for item, node in env.resource_nodes.items()} for env in self.world
            ],
        }
        save_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Game saved to {save_path}.")

    def load_game(self, filename: str) -> None:
        """Load a prior save file and restore player and world progression."""
        save_path = Path(filename)
        if not save_path.exists():
            print(f"No save file found at {save_path}.")
            return

        payload = json.loads(save_path.read_text(encoding="utf-8"))
        player_data = payload["player"]
        shelter_data = player_data.pop("shelter")
        self.player = Player(**player_data)
        self.player.shelter = Shelter(**shelter_data)
        self.weather = Weather(**payload["weather"])

        season_data = payload.get("season")
        if season_data:
            self.season_index = season_data["index"] % len(self.seasons)
            self.season_timer = season_data["timer"]
        else:
            self.season_index = 0
            self.season_timer = 0
        self.current_season = self.seasons[self.season_index]

        event_data = payload.get("event", {})
        active = event_data.get("active") if isinstance(event_data, dict) else None
        self.active_event = Event(**active) if active else None
        self.event_timer = event_data.get("timer", 0) if isinstance(event_data, dict) else 0
        self.event_check_timer = event_data.get("check_timer", 0) if isinstance(event_data, dict) else 0

        for env, env_nodes in zip(self.world, payload["world_nodes"]):
            for item, node_data in env_nodes.items():
                env.resource_nodes[item] = ResourceNode(**node_data)
        print(f"Game loaded from {save_path}.")

    def help(self) -> None:
        print(
            """
Commands:
 look, status, inventory
 gather, hunt, drink, eat, rest, travel
 craft <item>   (rope, spark_crystal, campfire, lean-to, hut)
 cook, extinguish, save [file], load [file], help, quit
"""
        )

    def run(self) -> None:
        print("\n🌲 Campfire Cantos: a tiny survival fantasy 🌲")
        print("You awaken with one stone, one stick, and a clear need to make practical choices.")
        self.describe_location()
        self.help()

        while self.running:
            self.status()
            cmd = input("\n> ").strip().lower()
            if not cmd:
                continue
            self.execute_command(cmd)


def main() -> None:
    SurvivalGame().run()


if __name__ == "__main__":
    main()
    
            """
Commands:
 look, status, inventory
 gather, hunt, drink, eat, rest, travel
 craft <item>   (rope, spark_crystal, campfire, lean-to, hut)
 cook, extinguish, save [file], load [file], help, quit
"""
        )

    def run(self) -> None:
        print("\n🌲 Campfire Cantos: a tiny survival fantasy 🌲")
        print("You awaken with one stone, one stick, and too much confidence.")
        self.describe_location()
        self.help()

        while self.running:
            self.status()
            cmd = input("\n> ").strip().lower()
            if not cmd:
                continue
            self.execute_command(cmd)


def main() -> None:
    SurvivalGame().run()


if __name__ == "__main__":
    main()

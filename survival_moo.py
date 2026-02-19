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
    """Tracks local gatherable resources with depletion and regeneration behavior."""

    item: str
    count: int
    max_count: int
    regen_rate: int

    def harvest(self, amount: int) -> int:
        """Take up to `amount` resources from the node and return actual harvested quantity."""
        taken = min(self.count, amount)
        self.count -= taken
        return taken

    def regenerate(self) -> None:
        """Regenerate this node by its configured regen rate each world tick."""
        self.count = min(self.max_count, self.count + self.regen_rate)


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


@dataclass
class Weather:
    name: str
    temperature_shift: int
    thirst_rate: int
    fire_modifier: float
    hunt_modifier: float
    mood: str


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


class SurvivalGame:
    """Main game object that owns world state and executes command actions."""

    def __init__(self) -> None:
        self.world = self._load_world_from_data(WORLD_DATA)
        self.weather_types = self._load_weather_from_data(WEATHER_DATA)
        self.player = Player(location=random.randint(0, len(self.world) - 1))
        self.weather = random.choice(self.weather_types)
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
                        )
                        for item, node in entry["resource_nodes"].items()
                    },
                )
            )
        return world

    def _load_weather_from_data(self, weather_data: List[dict]) -> List[Weather]:
        """Build Weather objects from data definitions."""
        return [Weather(**entry) for entry in weather_data]

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
        print(env.flavor)
        print(f"Weather: {self.weather.name} — {self.weather.mood}")
        print("Points of interest:")
        for p in env.pois:
            print(f" - {p.name}: {p.description}")
        print("Water sources:")
        for w in env.water_sources:
            print(f" - {w.name} ({w.quality}): {w.description}")

    def status(self) -> None:
        p = self.player
        print(
            f"\nHealth:{p.health} Hunger:{p.hunger}/100 Thirst:{p.thirst}/100 "
            f"BodyTemp:{p.body_temp}C Time:{p.hours:02d}:00"
        )
        print(f"Shelter: {p.shelter.label} | Fire: {'lit' if p.fire_lit else 'out'}")
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

    def _regenerate_world_resources(self, hrs: int) -> None:
        """Regenerate resources in all environments per hour to keep exploration valuable."""
        for _ in range(hrs):
            for env in self.world:
                for node in env.resource_nodes.values():
                    node.regenerate()

    def _update_fire_from_weather(self) -> None:
        """Weather can extinguish or stabilize fire depending on fire_modifier."""
        if not self.player.fire_lit:
            return
        failure_chance = max(0.0, 0.12 - self.weather.fire_modifier)
        if random.random() < failure_chance:
            self.player.fire_lit = False
            print("The weather smothers your fire. The embers sigh dramatically.")

    def advance_time(self, hrs: int = 1) -> None:
        p = self.player
        env = self.current_env()
        p.hours = (p.hours + hrs) % 24
        if random.random() < 0.35:
            self.weather = random.choice(self.weather_types)
            print(f"\nWeather shift! It is now {self.weather.name.lower()}.")

        # Balanced baseline progression: hunger rises more slowly than thirst.
        p.hunger = min(100, p.hunger + (2 + max(0, self.weather.thirst_rate // 2)) * hrs)
        p.thirst = min(100, p.thirst + (3 + self.weather.thirst_rate) * hrs)
        ambient_temp = 37 + env.temp_bias + self.weather.temperature_shift

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
        self.resolve_survival()

    def resolve_survival(self) -> None:
        p = self.player
        if p.hunger >= 90:
            p.health -= 2
            print("You are starving. Your stomach sounds like an angry troll.")
        if p.thirst >= 90:
            p.health -= 3
            print("You are dangerously dehydrated. Your tongue feels like old parchment.")
        if p.body_temp <= 34:
            p.health -= 5
            print("Hypothermia risk! You're shivering hard.")
        if p.body_temp >= 40:
            p.health -= 5
            print("Hyperthermia risk! Your head swims in the heat.")

        p.body_temp = max(30, min(42, p.body_temp))
        if p.health <= 0:
            print("\nYou collapse. A passing wizard leaves you a stern note about hydration.")
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
            print(f"The nearby {node.item} patch is temporarily depleted.")
        self.advance_time()

    def hunt(self) -> None:
        env = self.current_env()
        target = random.choice(env.huntables)
        has_rope = self.player.inventory.get("rope", 0) > 0
        base_success = 0.45 + (0.15 if has_rope else 0)
        success = max(0.1, min(0.9, base_success + self.weather.hunt_modifier))
        if random.random() < success:
            meat = random.randint(1, 3)
            hide = random.randint(0, 2)
            self.player.inventory["raw_meat"] += meat
            self.player.inventory["hide"] += hide
            print(f"Successful hunt: {target}. You get {meat} raw meat and {hide} hide.")
        else:
            print(f"The {target} escapes in the {self.weather.name.lower()} weather.")
        self.advance_time(2)

    def drink(self) -> None:
        env = self.current_env()
        source = random.choice(env.water_sources)
        print(f"You drink from {source.name}.")
        if source.quality in {"murky", "muddy", "risky", "salty"} and random.random() < 0.25:
            self.player.health -= 5
            print("Uh oh. That water was sketchy. You feel ill.")
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
            print("You build a campfire. Cozy points +10.")
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
            print("You roast a mushroom cap. Smells surprisingly noble.")
        print(f"You cook {cooked} meat over the fire.")
        self.advance_time(1)

    def eat(self) -> None:
        inv = self.player.inventory
        if inv["cooked_meat"] > 0:
            inv["cooked_meat"] -= 1
            self.player.hunger = max(0, self.player.hunger - 35)
            print("You eat cooked meat. Delicious and not screamingly raw.")
        elif inv["berries"] > 0:
            inv["berries"] -= 1
            self.player.hunger = max(0, self.player.hunger - 15)
            print("You snack on berries.")
        elif inv["mushroom"] > 0:
            inv["mushroom"] -= 1
            self.player.hunger = max(0, self.player.hunger - 10)
            print("You nibble a mushroom. It's either fine or magically adventurous.")
        else:
            print("You have nothing edible right now.")
            return
        self.advance_time(1)

    def rest(self) -> None:
        heal = 8 + (4 * self.player.shelter.level)
        if self.player.fire_lit:
            heal += 4
        self.player.health = min(100, self.player.health + heal)
        print(f"You rest for a while and recover {heal} health.")
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

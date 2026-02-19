#!/usr/bin/env python3
"""
Campfire Cantos: a text survival game with light fantasy vibes.
Inspired by old-school MUD command loops.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class WaterSource:
    name: str
    quality: str
    description: str


@dataclass
class Poi:
    name: str
    description: str


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


@dataclass
class Weather:
    name: str
    temperature_shift: int
    thirst_rate: int
    fire_modifier: int
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
        "water": 1,
        "spark_crystal": 0,
        "hide": 0,
        "rope": 0,
    })
    shelter: Shelter = field(default_factory=Shelter)
    fire_lit: bool = False


class SurvivalGame:
    def __init__(self) -> None:
        self.world = self._build_world()
        self.player = Player(location=random.randint(0, len(self.world) - 1))
        self.weather = random.choice(self._weather_types())
        self.running = True

    def _weather_types(self) -> List[Weather]:
        return [
            Weather("Clear", 0, 0, 0, "The sky is crystal blue and suspiciously optimistic."),
            Weather("Rain", -2, -1, -1, "Gentle rain patters like tiny drummers on leaves."),
            Weather("Storm", -4, 1, -2, "Thunder shouts dramatic monologues across the valley."),
            Weather("Heatwave", 4, 2, 0, "The air shimmers; even rocks look sweaty."),
            Weather("Frostwind", -6, 1, 1, "A razor wind whistles through every seam in your clothing."),
            Weather("Fairy Mist", -1, 0, 1, "Minty fog glows with tiny lights and giggling sprites."),
        ]

    def _build_world(self) -> List[Environment]:
        return [
            Environment(
                name="Emerald Pinewood",
                terrain="Dense conifer forest",
                flavor="Towering pines sway overhead; resin and moss perfume the air.",
                gatherables=["stick", "fiber", "mushroom", "berries"],
                huntables=["hare", "boar"],
                water_sources=[
                    WaterSource("Needlebrook", "clear", "A cold brook threading between roots."),
                    WaterSource("Dew Pools", "clean", "Shallow pools that glitter in morning shade."),
                ],
                pois=[
                    Poi("Whisperfall", "A small waterfall hidden behind fern curtains."),
                    Poi("Moonroot Hollow", "A cave where roots glow silver at dusk."),
                ],
                temp_bias=-1,
            ),
            Environment(
                name="Sunfire Canyon",
                terrain="Red-rock canyon",
                flavor="Sheer walls blaze orange at noon and purple at dusk.",
                gatherables=["stone", "fiber", "berries"],
                huntables=["lizard", "goat"],
                water_sources=[
                    WaterSource("Dripstone Basin", "risky", "A mineral pool fed by cave drips."),
                    WaterSource("Flash Creek", "muddy", "An intermittent stream that appears after rain."),
                ],
                pois=[
                    Poi("Echo Arch", "A natural stone arch that repeats your worst jokes."),
                    Poi("Skytooth Overlook", "A narrow ledge with vast canyon views."),
                ],
                temp_bias=3,
            ),
            Environment(
                name="Frostglass Tundra",
                terrain="Wind-blasted tundra",
                flavor="Snow crust sparkles like crushed glass under pale light.",
                gatherables=["stick", "fiber", "mushroom"],
                huntables=["elk", "fox"],
                water_sources=[
                    WaterSource("Melt Rill", "cold", "A stream from thawing blue ice."),
                    WaterSource("Ice Lens", "clean", "Clear meltwater trapped in ancient ice."),
                ],
                pois=[
                    Poi("Aurora Spire", "A jagged tower where lights dance every night."),
                    Poi("Howl Cavern", "An icy cave that sings in the wind."),
                ],
                temp_bias=-6,
            ),
            Environment(
                name="Mossmere Wetlands",
                terrain="Boggy marsh",
                flavor="Mist drifts over reeds while frogs hold rowdy choir practice.",
                gatherables=["fiber", "berries", "mushroom"],
                huntables=["duck", "deer"],
                water_sources=[
                    WaterSource("Reedwater", "murky", "Brown still water tangled in reeds."),
                    WaterSource("Sprite Spring", "clear", "A tiny spring guarded by polite dragonflies."),
                ],
                pois=[
                    Poi("Singing Bog", "A peat field that bubbles in eerie melodies."),
                    Poi("Lantern Stumps", "Old tree stumps glowing with bioluminescent fungi."),
                ],
                temp_bias=0,
            ),
            Environment(
                name="Starfall Coast",
                terrain="Rocky coastline",
                flavor="Waves crash against black cliffs, flinging silver spray skyward.",
                gatherables=["stone", "fiber", "berries"],
                huntables=["crab", "seal"],
                water_sources=[
                    WaterSource("Rain Cistern", "clean", "A naturally carved basin collecting rainwater."),
                    WaterSource("Cliff Seep", "salty", "Trickling water near sea spray; questionable taste."),
                ],
                pois=[
                    Poi("Tide Caves", "Sea caves with phosphorescent walls."),
                    Poi("Comet Watch", "A promontory where meteors streak overhead."),
                ],
                temp_bias=1,
            ),
        ]

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

    def inventory(self) -> None:
        print("\nInventory:")
        for item, count in sorted(self.player.inventory.items()):
            if count > 0:
                print(f" - {item}: {count}")

    def advance_time(self, hrs: int = 1) -> None:
        p = self.player
        env = self.current_env()
        p.hours = (p.hours + hrs) % 24
        if random.random() < 0.35:
            self.weather = random.choice(self._weather_types())
            print(f"\nWeather shift! It is now {self.weather.name.lower()}.")

        p.hunger = min(100, p.hunger + 4 * hrs)
        p.thirst = min(100, p.thirst + (5 + self.weather.thirst_rate) * hrs)
        ambient_temp = 37 + env.temp_bias + self.weather.temperature_shift

        if p.fire_lit:
            p.body_temp += 1
        else:
            if ambient_temp < 33:
                p.body_temp -= 1
            elif ambient_temp > 40:
                p.body_temp += 1

        if p.shelter.level > 0:
            p.body_temp += 1 if ambient_temp < 35 else -1 if ambient_temp > 39 else 0

        self.resolve_survival()

    def resolve_survival(self) -> None:
        p = self.player
        if p.hunger >= 90:
            p.health -= 3
            print("You are starving. Your stomach sounds like an angry troll.")
        if p.thirst >= 90:
            p.health -= 4
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
        item = random.choice(env.gatherables)
        amount = random.randint(1, 3)
        self.player.inventory[item] += amount
        print(f"You gather {amount} x {item} from the {env.terrain.lower()}.")
        self.advance_time()

    def hunt(self) -> None:
        env = self.current_env()
        target = random.choice(env.huntables)
        success = 0.6 if "rope" in self.player.inventory and self.player.inventory["rope"] > 0 else 0.45
        if random.random() < success:
            meat = random.randint(1, 3)
            hide = random.randint(0, 2)
            self.player.inventory["raw_meat"] += meat
            self.player.inventory["hide"] += hide
            print(f"Successful hunt: {target}. You get {meat} raw meat and {hide} hide.")
        else:
            print(f"The {target} escapes and probably mocks your technique.")
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

    def help(self) -> None:
        print(
            """
Commands:
 look, status, inventory
 gather, hunt, drink, eat, rest, travel
 craft <item>   (rope, spark_crystal, campfire, lean-to, hut)
 cook, extinguish, help, quit
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
            if cmd == "quit":
                print("You leave the wilderness with stories and at least one mysterious rash.")
                break
            if cmd == "help":
                self.help()
            elif cmd == "look":
                self.describe_location()
            elif cmd == "status":
                self.status()
            elif cmd == "inventory":
                self.inventory()
            elif cmd == "gather":
                self.gather()
            elif cmd == "hunt":
                self.hunt()
            elif cmd == "drink":
                self.drink()
            elif cmd == "eat":
                self.eat()
            elif cmd == "cook":
                self.cook()
            elif cmd.startswith("craft "):
                self.craft(cmd.removeprefix("craft ").strip())
            elif cmd == "travel":
                self.travel()
            elif cmd == "rest":
                self.rest()
            elif cmd == "extinguish":
                self.extinguish()
            else:
                print("Unknown command. Type 'help' for options.")


def main() -> None:
    SurvivalGame().run()


if __name__ == "__main__":
    main()

"""Static world and weather data for Campfire Cantos."""

WORLD_DATA = [
    {
        "name": "Emerald Pinewood",
        "terrain": "Dense conifer forest",
        "flavor": "Towering pines sway overhead; resin and moss perfume the air.",
        "gatherables": ["stick", "fiber", "mushroom", "berries"],
        "huntables": ["hare", "boar"],
        "water_sources": [
            {"name": "Needlebrook", "quality": "clear", "description": "A cold brook threading between roots."},
            {"name": "Dew Pools", "quality": "clean", "description": "Shallow pools that glitter in morning shade."},
        ],
        "pois": [
            {"name": "Whisperfall", "description": "A small waterfall hidden behind fern curtains."},
            {"name": "Moonroot Hollow", "description": "A cave where roots glow silver at dusk."},
        ],
        "temp_bias": -1,
        "resource_nodes": {
            "stick": {"max": 10, "count": 8, "regen": 2},
            "fiber": {"max": 8, "count": 6, "regen": 2},
            "mushroom": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 7, "count": 5, "regen": 1},
        },
    },
    {
        "name": "Sunfire Canyon",
        "terrain": "Red-rock canyon",
        "flavor": "Sheer walls blaze orange at noon and purple at dusk.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["lizard", "goat"],
        "water_sources": [
            {"name": "Dripstone Basin", "quality": "risky", "description": "A mineral pool fed by cave drips."},
            {"name": "Flash Creek", "quality": "muddy", "description": "An intermittent stream that appears after rain."},
        ],
        "pois": [
            {"name": "Echo Arch", "description": "A natural stone arch that repeats your worst jokes."},
            {"name": "Skytooth Overlook", "description": "A narrow ledge with vast canyon views."},
        ],
        "temp_bias": 3,
        "resource_nodes": {
            "stone": {"max": 10, "count": 9, "regen": 2},
            "fiber": {"max": 5, "count": 4, "regen": 1},
            "berries": {"max": 4, "count": 3, "regen": 1},
        },
    },
    {
        "name": "Frostglass Tundra",
        "terrain": "Wind-blasted tundra",
        "flavor": "Snow crust sparkles like crushed glass under pale light.",
        "gatherables": ["stick", "fiber", "mushroom"],
        "huntables": ["elk", "fox"],
        "water_sources": [
            {"name": "Melt Rill", "quality": "cold", "description": "A stream from thawing blue ice."},
            {"name": "Ice Lens", "quality": "clean", "description": "Clear meltwater trapped in ancient ice."},
        ],
        "pois": [
            {"name": "Aurora Spire", "description": "A jagged tower where lights dance every night."},
            {"name": "Howl Cavern", "description": "An icy cave that sings in the wind."},
        ],
        "temp_bias": -6,
        "resource_nodes": {
            "stick": {"max": 5, "count": 3, "regen": 1},
            "fiber": {"max": 5, "count": 3, "regen": 1},
            "mushroom": {"max": 4, "count": 2, "regen": 1},
        },
    },
    {
        "name": "Mossmere Wetlands",
        "terrain": "Boggy marsh",
        "flavor": "Mist drifts over reeds while frogs hold rowdy choir practice.",
        "gatherables": ["fiber", "berries", "mushroom"],
        "huntables": ["duck", "deer"],
        "water_sources": [
            {"name": "Reedwater", "quality": "murky", "description": "Brown still water tangled in reeds."},
            {"name": "Sprite Spring", "quality": "clear", "description": "A tiny spring guarded by polite dragonflies."},
        ],
        "pois": [
            {"name": "Singing Bog", "description": "A peat field that bubbles in eerie melodies."},
            {"name": "Lantern Stumps", "description": "Old tree stumps glowing with bioluminescent fungi."},
        ],
        "temp_bias": 0,
        "resource_nodes": {
            "fiber": {"max": 9, "count": 7, "regen": 2},
            "berries": {"max": 6, "count": 4, "regen": 1},
            "mushroom": {"max": 8, "count": 6, "regen": 2},
        },
    },
    {
        "name": "Starfall Coast",
        "terrain": "Rocky coastline",
        "flavor": "Waves crash against black cliffs, flinging silver spray skyward.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["crab", "seal"],
        "water_sources": [
            {"name": "Rain Cistern", "quality": "clean", "description": "A naturally carved basin collecting rainwater."},
            {"name": "Cliff Seep", "quality": "salty", "description": "Trickling water near sea spray; questionable taste."},
        ],
        "pois": [
            {"name": "Tide Caves", "description": "Sea caves with phosphorescent walls."},
            {"name": "Comet Watch", "description": "A promontory where meteors streak overhead."},
        ],
        "temp_bias": 1,
        "resource_nodes": {
            "stone": {"max": 10, "count": 8, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 5, "count": 3, "regen": 1},
        },
    },
]

WEATHER_DATA = [
    {"name": "Clear", "temperature_shift": 0, "thirst_rate": 0, "fire_modifier": 0, "hunt_modifier": 0.0,
     "mood": "The sky is crystal blue and suspiciously optimistic."},
    {"name": "Rain", "temperature_shift": -2, "thirst_rate": -1, "fire_modifier": -0.15, "hunt_modifier": -0.05,
     "mood": "Gentle rain patters like tiny drummers on leaves."},
    {"name": "Storm", "temperature_shift": -4, "thirst_rate": 1, "fire_modifier": -0.35, "hunt_modifier": -0.2,
     "mood": "Thunder shouts dramatic monologues across the valley."},
    {"name": "Heatwave", "temperature_shift": 4, "thirst_rate": 2, "fire_modifier": 0.1, "hunt_modifier": -0.1,
     "mood": "The air shimmers; even rocks look sweaty."},
    {"name": "Frostwind", "temperature_shift": -6, "thirst_rate": 1, "fire_modifier": 0.2, "hunt_modifier": -0.05,
     "mood": "A razor wind whistles through every seam in your clothing."},
    {"name": "Fairy Mist", "temperature_shift": -1, "thirst_rate": 0, "fire_modifier": 0.05, "hunt_modifier": 0.1,
     "mood": "Minty fog glows with tiny lights and giggling sprites."},
]

"""Static world and weather data for Campfire Cantos."""

WORLD_DATA = [
    {
        "name": "Emerald Pinewood",
        "terrain": "Dense conifer forest",
        "flavor": "Tall pines stand in close ranks and carry wind as a low canopy hiss. | Needle litter, moss pads, and old cones cover the forest floor between roots and fern patches. | Footing alternates between springy duff and slick logs, with hidden runoff channels after rain. | Filtered light shifts in vertical bands and keeps long-distance visibility short under mist.",
        "gatherables": ["stick", "fiber", "mushroom", "berries"],
        "huntables": ["hare", "boar", "fox", "deer"],
        "water_sources": [
            {"name": "Needlebrook", "quality": "clear", "description": "Cold flow over gravel keeps sediment low except after storms."},
            {"name": "Dew Pools", "quality": "clean", "description": "Shallow rain-fed pools are clear early, with leaf debris gathering near edges."},
        ],
        "pois": [
            {"name": "Whisperfall", "description": "A narrow fall drops onto slick basalt and masks nearby movement with steady noise."},
            {"name": "Moonroot Hollow", "description": "A root-bound cavity stays dry in light rain; some fibers show a faint silver glow at dusk."},
        ],
        "temp_bias": -1,
        "resource_nodes": {
            "stick": {"max": 10, "count": 8, "regen": 2},
            "fiber": {"max": 8, "count": 6, "regen": 2},
            "mushroom": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 7, "count": 5, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Wind moves high in the canopy; lower branches barely stir.",
                "A woodpecker taps in short bursts, then falls quiet.",
            ],
            "night": [
                "Needles shift softly and distant water keeps a steady line of sound.",
                "Small branch cracks carry farther in the cool air.",
            ],
            "winter": [
                "Frozen bark creaks in the cold and the brook runs quieter under edge ice.",
            ],
            "storm": [
                "Rain drums on needles while runoff gathers in shallow rills.",
            ],
        },
    },
    {
        "name": "Sunfire Canyon",
        "terrain": "Red-rock canyon",
        "flavor": "Red walls rise in layered tiers that hold heat past sunset. | Scrub plants root in ledges while the floor shifts between sand, shale chips, and talus fans. | Travel is quick on hardpack and slow on loose scree where footing rolls under weight. | Heat shimmer softens distant edges and reflected light brightens exposed routes.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["lizard", "goat", "fox"],
        "water_sources": [
            {"name": "Dripstone Basin", "quality": "risky", "description": "Slow drips collect in a mineral bowl; clear appearance hides metallic taste."},
            {"name": "Flash Creek", "quality": "muddy", "description": "After upstream rain, silt-heavy water arrives quickly and settles only after calm."},
        ],
        "pois": [
            {"name": "Echo Arch", "description": "A freestanding span reflects short calls in distinct beats with a measurable delay."},
            {"name": "Skytooth Overlook", "description": "A fractured ledge gives broad flood-channel views but exposes you to strong crosswind."},
        ],
        "temp_bias": 3,
        "resource_nodes": {
            "stone": {"max": 10, "count": 9, "regen": 2},
            "fiber": {"max": 5, "count": 4, "regen": 1},
            "berries": {"max": 4, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Pebbles click downslope where talus shifts under heat expansion.",
                "Wind passes the arch in short pulses and throws back clipped echoes.",
            ],
            "night": [
                "Rock radiates stored warmth while distant runoff drops in isolated drips.",
            ],
            "winter": [
                "Cold air sinks into the gorge and carries sound along the walls.",
            ],
            "storm": [
                "Thunder rolls in layers and sand channels begin to hiss with runoff.",
            ],
        },
    },
    {
        "name": "Frostglass Tundra",
        "terrain": "Wind-blasted tundra",
        "flavor": "Open ground stretches with little shelter and constant crosswind. | Snow crust, gravel, and lichen mats dominate with sparse low shrubs in dips. | Travel is efficient on firm crust but costly when drifts break underfoot. | Spindrift can erase detail in bands even when the sky remains bright.",
        "gatherables": ["stick", "fiber", "mushroom"],
        "huntables": ["elk", "fox", "hare"],
        "water_sources": [
            {"name": "Melt Rill", "quality": "cold", "description": "Near-freezing surface flow runs from blue ice and forms slush at the margins."},
            {"name": "Ice Lens", "quality": "clean", "description": "Clear pooled meltwater remains usable in daylight before rapid evening refreeze."},
        ],
        "pois": [
            {"name": "Aurora Spire", "description": "A dark rock spire collects rime; faint moving lights are sometimes observed overhead."},
            {"name": "Howl Cavern", "description": "Wind-cut slots in an ice cave produce long tonal hums that change with direction."},
        ],
        "temp_bias": -6,
        "resource_nodes": {
            "stick": {"max": 5, "count": 3, "regen": 1},
            "fiber": {"max": 5, "count": 3, "regen": 1},
            "mushroom": {"max": 4, "count": 2, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Fine snow grains skim the crust in steady, low lines.",
                "Boot pressure cracks the surface in dry, sharp snaps.",
            ],
            "night": [
                "Wind crosses open ground without interruption and carries a hollow edge tone.",
            ],
            "winter": [
                "Ice crystals hiss across exposed rock and fabric stiffens quickly.",
            ],
            "storm": [
                "Blowing snow muffles distance and direction while gusts surge in waves.",
            ],
        },
    },
    {
        "name": "Mossmere Wetlands",
        "terrain": "Boggy marsh",
        "flavor": "Peat flats and reed channels spread across low ground with standing water. | Sedge hummocks, cattails, and moss mats break the surface into narrow paths. | Footing shifts from firm islands to soft pockets with little warning. | Fog sits low at dawn and carries tannin-rich wet-earth odor.",
        "gatherables": ["fiber", "berries", "mushroom"],
        "huntables": ["duck", "deer", "hare"],
        "water_sources": [
            {"name": "Reedwater", "quality": "murky", "description": "Still brown water holds peat fines and strong tannin stain near reed roots."},
            {"name": "Sprite Spring", "quality": "clear", "description": "A gravel upwelling remains clear but attracts dense insects at calm dusk."},
        ],
        "pois": [
            {"name": "Singing Bog", "description": "Gas vents bubble through saturated peat and can collapse under focused weight."},
            {"name": "Lantern Stumps", "description": "Bioluminescent fungus on drowned stumps gives a steady green route marker at night."},
        ],
        "temp_bias": 0,
        "resource_nodes": {
            "fiber": {"max": 9, "count": 7, "regen": 2},
            "berries": {"max": 6, "count": 4, "regen": 1},
            "mushroom": {"max": 8, "count": 6, "regen": 2},
        },
        "soundscape": {
            "day": [
                "Reed stems click in crosswind while insects hold a constant high buzz.",
                "Mud releases slow bubbles where sunlight warms shallow pools.",
            ],
            "night": [
                "Frog calls spread in uneven layers across channels and open pools.",
            ],
            "winter": [
                "Thin ice skins over side pools and reeds knock gently in dry wind.",
            ],
            "storm": [
                "Rain flattens the water surface and overflow channels begin to connect.",
            ],
        },
    },
    {
        "name": "Starfall Coast",
        "terrain": "Rocky coastline",
        "flavor": "Black basalt shelves descend toward cold surf and constant spray. | Coarse sand, salt grass, and tide wrack collect between rock ribs and barnacle bands. | Wet basalt becomes slick quickly; safe return routes narrow with incoming tide. | Air carries salt and iron while sea mist reduces detail near cliff bases.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["crab", "seal", "fox"],
        "water_sources": [
            {"name": "Rain Cistern", "quality": "clean", "description": "A sheltered basin captures rainwater and stays clear when recently replenished."},
            {"name": "Cliff Seep", "quality": "salty", "description": "A spray-fed seep crosses salt crust and tastes distinctly brackish."},
        ],
        "pois": [
            {"name": "Tide Caves", "description": "Basalt chambers brighten with faint blue bioluminescent films when foam disturbs wet walls."},
            {"name": "Comet Watch", "description": "An exposed point offers wide sky views but strong wind complicates open fires."},
        ],
        "temp_bias": 1,
        "resource_nodes": {
            "stone": {"max": 10, "count": 8, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Wave wash drags rounded stones with a steady grinding pull.",
                "Spray strikes cliff faces in sharp bursts that fade to hiss.",
            ],
            "night": [
                "Tide caves breathe with each set while wind moves across open water.",
            ],
            "winter": [
                "Cold surf throws finer spray and leaves salt crust on exposed gear.",
            ],
            "storm": [
                "Heavy sets slam the shelves and retreat with a deep rattling draw.",
            ],
        },
    },
    {
        "name": "Pinewood Edge",
        "terrain": "Forest-meadow transition",
        "flavor": "Conifers thin into open grass patches with mixed shrub cover. | Needles give way to damp soil and low flowers in sun gaps. | Footing is easier than deep forest but slick along shaded roots. | Visibility opens enough to track movement between tree line and field edge.",
        "gatherables": ["stick", "fiber", "berries", "mushroom"],
        "huntables": ["hare", "deer", "fox"],
        "water_sources": [
            {"name": "Edge Run", "quality": "clear", "description": "A shallow run exits the woods with moderate flow and visible pebbled bed."},
            {"name": "Field Swale", "quality": "clean", "description": "Seasonal lowland pooling remains clear after dry spells and clouds after heavy trampling."},
        ],
        "pois": [
            {"name": "Split Treeline", "description": "Windbreak pines form a natural lee where meadow and woods meet."},
            {"name": "Fox Tracks", "description": "Fresh crossings repeat at dawn and dusk where game paths converge."},
        ],
        "temp_bias": 0,
        "resource_nodes": {
            "stick": {"max": 8, "count": 6, "regen": 2},
            "fiber": {"max": 8, "count": 6, "regen": 2},
            "berries": {"max": 7, "count": 5, "regen": 1},
            "mushroom": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": ["Grass heads brush together while canopy noise fades behind you."],
            "night": ["Open ground carries small hoof steps farther than expected."],
            "winter": ["Frozen grass rasps in light wind near the treeline."],
            "storm": ["Rain moves from the trees into open field in visible sheets."],
        },
    },
    {
        "name": "High Scrub",
        "terrain": "Canyon-tundra transition",
        "flavor": "Broken red stone rises into colder, wind-exposed benches. | Low shrubs and hardy grasses cling to shallow pockets of soil. | Talus fields interrupt direct travel and force contour routes. | Air alternates between dry heat and sharp chill as elevation shifts.",
        "gatherables": ["stone", "fiber", "stick"],
        "huntables": ["goat", "fox", "hare", "lizard"],
        "water_sources": [
            {"name": "Bench Seep", "quality": "risky", "description": "Intermittent seep flow appears clear but carries mineral-heavy taste."},
            {"name": "Snow Runnel", "quality": "cold", "description": "Seasonal melt cuts narrow channels along shaded slopes."},
        ],
        "pois": [
            {"name": "Wind Notch", "description": "A narrow pass amplifies gusts and quickly strips heat from exposed skin."},
            {"name": "Shard Flats", "description": "Fragments of red shale create loud, unstable footing over broad ground."},
        ],
        "temp_bias": -2,
        "resource_nodes": {
            "stone": {"max": 9, "count": 7, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "stick": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": ["Loose shale ticks downslope under intermittent wind pulses."],
            "night": ["Cold air funnels through rock cuts in a long, narrow tone."],
            "winter": ["Spindrift skates over stone benches and gathers in shallow drifts."],
            "storm": ["Gust fronts push grit across exposed shelves with a dry hiss."],
        },
    },
    {
        "name": "Reed Margin",
        "terrain": "Wetland-forest transition",
        "flavor": "A wet fringe of reeds and alder roots surrounds shallow channels. | Mossy logs and peat banks alternate with firmer stands of young trees. | Movement is passable but still requires probing near dark water pockets. | Morning haze lingers between trunks and open marsh lanes.",
        "gatherables": ["fiber", "berries", "mushroom", "stick"],
        "huntables": ["duck", "deer", "hare", "boar"],
        "water_sources": [
            {"name": "Alder Flow", "quality": "clear", "description": "Slow stream threads through roots with moderate tannin tint but low sediment."},
            {"name": "Backwater Pocket", "quality": "murky", "description": "Stagnant side pocket collects plant fines and algae film in warm periods."},
        ],
        "pois": [
            {"name": "Root Causeway", "description": "An old root mat gives one of the few reliable crossings above knee-deep mud."},
            {"name": "Mist Lamp Fungus", "description": "Pale fungus on soaked bark gives a weak steady glow in low light."},
        ],
        "temp_bias": -1,
        "resource_nodes": {
            "fiber": {"max": 9, "count": 7, "regen": 2},
            "berries": {"max": 6, "count": 4, "regen": 1},
            "mushroom": {"max": 7, "count": 5, "regen": 2},
            "stick": {"max": 7, "count": 5, "regen": 1},
        },
        "soundscape": {
            "day": ["Water drips from alder roots while reed tops rattle in side wind."],
            "night": ["Frog calls fade into forest insect chatter at the margin."],
            "winter": ["Thin ice rings softly around root channels when brushed by current."],
            "storm": ["Overflow links side pools and turns narrow paths into shallow sheets."],
        },
    },
    {
        "name": "Pebble Strand",
        "terrain": "Coast-upland transition",
        "flavor": "Rounded stone beaches rise toward scrub-covered upland slopes. | Salt grass and low brush mix with driftwood above the tide line. | Pebble footing shifts under load but drains quickly after rain. | Wind is persistent but less severe than the exposed headlands.",
        "gatherables": ["stone", "fiber", "stick", "berries"],
        "huntables": ["crab", "fox", "deer"],
        "water_sources": [
            {"name": "Drift Basin", "quality": "clean", "description": "Rainwater gathers behind a driftwood berm and remains fresh between storms."},
            {"name": "Foam Sluice", "quality": "salty", "description": "Wave splash fills a shallow runnel with brackish water and suspended sand."},
        ],
        "pois": [
            {"name": "Shingle Fan", "description": "A broad fan of rounded stones records recent storm height and wave reach."},
            {"name": "Windbreak Bluff", "description": "A low bluff gives partial shelter for fire maintenance above spray range."},
        ],
        "temp_bias": 1,
        "resource_nodes": {
            "stone": {"max": 9, "count": 7, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "stick": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": ["Pebbles settle with each retreating wave in a rolling, granular rush."],
            "night": ["Wave sets arrive in long intervals while upland grass moves lightly."],
            "winter": ["Cold spray drifts inland and leaves a brittle salt edge on stone."],
            "storm": ["Breaking sets hammer the strand and throw grit across the upper bank."],
        },
    },
]

WEATHER_DATA = [
    {
        "name": "Clear",
        "temperature_shift": 0,
        "thirst_rate": 0,
        "fire_modifier": 0,
        "hunt_modifier": 0.0,
        "mood": "Cloud cover is minimal and winds remain light, so visibility stays long from ridge to low ground. Sunlight is direct through most of the day, with sharper shadow contrast in dense cover. Night cooling is noticeable in open terrain once the sky stays cloudless.",
    },
    {
        "name": "Rain",
        "temperature_shift": -2,
        "thirst_rate": -1,
        "fire_modifier": -0.15,
        "hunt_modifier": -0.05,
        "mood": "Low clouds seal in the sky while steady rain dampens fuel and softens distant detail. Footing degrades quickly on roots, stone, and packed soil as water films build. Sound carries differently under the rainfall hiss, which can hide movement until it is close.",
    },
    {
        "name": "Storm",
        "temperature_shift": -4,
        "thirst_rate": 1,
        "fire_modifier": -0.35,
        "hunt_modifier": -0.2,
        "mood": "Dark convective clouds stack fast, bringing hard rain, strong gust fronts, and abrupt pressure shifts. Thunder rolls for a long time after each strike and rebounds across terrain features, making distance hard to judge by sound alone. Visibility drops in bursts, and exposed routes become commitment-heavy in minutes.",
    },
    {
        "name": "Heatwave",
        "temperature_shift": 4,
        "thirst_rate": 2,
        "fire_modifier": 0.1,
        "hunt_modifier": -0.1,
        "mood": "Hot, dry air settles in with thin cloud cover and persistent glare through midday. Heat shimmer wavers above stone and hard ground, blurring edges and hiding subtle movement at distance. Sweat loss climbs quickly in direct sun, and shade becomes practical strategy rather than luxury.",
    },
    {
        "name": "Frostwind",
        "temperature_shift": -6,
        "thirst_rate": 1,
        "fire_modifier": 0.2,
        "hunt_modifier": -0.05,
        "mood": "Subfreezing gusts drive fine ice grains across exposed ground and strip warmth from skin and wet fabric quickly. Visibility can remain high, but comfort does not negotiate and small tasks take longer with numb hands. Any pause out of shelter starts costing heat almost immediately.",
    },
    {
        "name": "Fairy Mist",
        "temperature_shift": -1,
        "thirst_rate": 0,
        "fire_modifier": 0.05,
        "hunt_modifier": 0.1,
        "mood": "Cool fog settles close to the ground and narrows sightlines to short, shifting windows between trunks, reeds, or rock. The air carries a mild sweet-ozone note, and faint points of light are occasionally visible at mid-distance with no clear source. They might be insects in reflected moisture; they might also decline to be explained on schedule.",
    },
]

"""Static world and weather data for Campfire Cantos."""

WORLD_DATA = [
    {
        "name": "Emerald Pinewood",
        "terrain": "Dense conifer forest",
        "flavor": "Tall conifers stand close enough that the canopy filters noon light into narrow green shafts, and the horizon shortens to the next line of trunks. Needles, cone scales, and damp bark fragments build a springy duff layer over acidic soil, while moss and bracket fungi mark the shaded side of fallen logs. In late warm seasons, berry shrubs and fern patches thicken along openings where windthrow let light in, and game trails become more visible in trampled understory. After rain, slick roots and water-dark wood make footing less certain than it first appears. Resin scent is strongest where bark has split, and cold air settles early in low hollows.",
        "gatherables": ["stick", "fiber", "mushroom", "berries"],
        "huntables": ["hare", "boar", "fox", "deer"],
        "water_sources": [
            {
                "name": "Needlebrook",
                "quality": "clear",
                "description": "A narrow, cold stream runs over rounded gravel with good oxygenation and low visible sediment in dry weather. Heavy rain can raise turbidity quickly, so clearest draws come from riffles after flow settles.",
            },
            {
                "name": "Dew Pools",
                "quality": "clean",
                "description": "Shallow depressions hold overnight condensation and light rainwater beneath conifer shade. They are usually clear at dawn but accumulate needles and insect activity by midday.",
            },
        ],
        "pois": [
            {
                "name": "Whisperfall",
                "description": "A thin waterfall drops over basalt into a compact plunge pocket lined with polished stone. Constant white noise masks footfall and small branch snaps, useful for concealment but poor for hearing approach.",
            },
            {
                "name": "Moonroot Hollow",
                "description": "An exposed root chamber under an overturned pine stays relatively dry in light rain and cuts wind from two sides. At dusk, pale root fibers can show a faint steady sheen, likely fungal or mineral reflection, though it is hard to confirm without close light.",
            },
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
                "Wind moves across upper needles while the understory stays almost still.",
                "A woodpecker taps in measured bursts, then goes quiet long enough to make you check your own breathing.",
            ],
            "night": [
                "Needle litter shifts under small ground movement, and water keeps a steady thread of sound downslope.",
                "A single owl call carries cleanly between trunks before the forest closes around it again.",
            ],
            "winter": [
                "Ice at stream margins clicks softly as current works beneath it.",
            ],
            "storm": [
                "Rain beads through layered branches and gathers into intermittent drips from bough tips.",
            ],
        },
    },
    {
        "name": "Sunfire Canyon",
        "terrain": "Red-rock canyon",
        "flavor": "Layered sandstone and shale hold heat well past sunset, and reflected light from pale walls can make midday feel brighter than the open plain. Sparse shrubs root in fracture lines, while coarse sand and talus aprons collect below steep faces where freeze-thaw and thermal cracking loosen stone. In dry periods, dust sits in shallow channels and lifts easily with gusts; after rain, those same channels become short-lived flow paths with undercut banks. Travel is fast on packed benches and slow on rolling scree where each step asks for balance. Echo timing is clear enough here to estimate distance, though the canyon is not always polite about accuracy.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["lizard", "goat", "fox"],
        "water_sources": [
            {
                "name": "Dripstone Basin",
                "quality": "risky",
                "description": "Slow dripwater accumulates in a mineral-lined bowl and often appears clear at first glance. Dissolved minerals leave a metallic taste and residue, so treatment is prudent before relying on it.",
            },
            {
                "name": "Flash Creek",
                "quality": "muddy",
                "description": "This channel activates quickly after upstream rainfall and carries high suspended silt loads. Water may look opaque for hours after peak flow, and banks can slump where fines settle.",
            },
        ],
        "pois": [
            {
                "name": "Echo Arch",
                "description": "A freestanding stone arch spans a narrow cut where sound reflects in crisp delayed returns. Short calls come back in distinct intervals that can help estimate wall spacing and wind direction.",
            },
            {
                "name": "Skytooth Overlook",
                "description": "A high fractured ledge provides long views of drainage lines, debris fans, and likely flood exits. Exposure is significant, and loose edge rock favors careful movement over fast movement.",
            },
        ],
        "temp_bias": 3,
        "resource_nodes": {
            "stone": {"max": 10, "count": 9, "regen": 2},
            "fiber": {"max": 5, "count": 4, "regen": 1},
            "berries": {"max": 4, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Pebbles click down talus faces as heat expansion loosens small fragments.",
                "Wind pulses through side cuts and returns as broken echoes from opposing walls.",
            ],
            "night": [
                "Stored heat leaves the rock slowly, and isolated drips mark shaded overhangs.",
            ],
            "winter": [
                "Cold air drains through narrow channels and sharpens every small stone strike.",
            ],
            "storm": [
                "Thunder rolls along parallel walls while runoff begins to braid through sand.",
            ],
        },
    },
    {
        "name": "Frostglass Tundra",
        "terrain": "Wind-blasted tundra",
        "flavor": "Open ground and low relief leave little shelter from prevailing wind, and visibility can stretch far until spindrift bands erase detail. Surface cover alternates between crusted snow, exposed gravel, and lichen mats that hold to shallow, nutrient-poor soil. Woody growth is sparse and low, with only occasional shrubs in depressions where drifting snow insulates roots. In cold clear weather, light reflects strongly from ice-polished patches and can hide subtle breaks in the surface. Travel stays efficient on firm crust but becomes energy-intensive the moment it collapses into hidden layers. Tracks persist clearly here when wind is low and vanish almost immediately when it rises.",
        "gatherables": ["stick", "fiber", "mushroom"],
        "huntables": ["elk", "fox", "hare"],
        "water_sources": [
            {
                "name": "Melt Rill",
                "quality": "cold",
                "description": "A thin melt channel runs from seasonal ice, near freezing and fast enough to stay mostly clear. Slush accumulates at edges in shade, reducing easy fill points.",
            },
            {
                "name": "Ice Lens",
                "quality": "clean",
                "description": "A clear pocket of meltwater forms in shallow ice basins with minimal sediment input. It can refreeze rapidly once sun drops or wind strengthens.",
            },
        ],
        "pois": [
            {
                "name": "Aurora Spire",
                "description": "A dark rock spire rises above the plain and gathers rime on its windward side. On clear nights, faint moving lights are sometimes observed near its upper margin, steady enough to notice and distant enough to stay unresolved.",
            },
            {
                "name": "Howl Cavern",
                "description": "A wind-cut ice chamber narrows into slots that convert gusts into long tonal resonance. Tone shifts can hint at changing wind direction before the weather front is obvious.",
            },
        ],
        "temp_bias": -6,
        "resource_nodes": {
            "stick": {"max": 5, "count": 3, "regen": 1},
            "fiber": {"max": 5, "count": 3, "regen": 1},
            "mushroom": {"max": 4, "count": 2, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Fine snow grains skim the surface in parallel lines where gusts stay consistent.",
                "Boot pressure cracks crust in short, dry reports that carry farther than expected.",
            ],
            "night": [
                "Wind crosses open ground without interruption and leaves a low edge tone in exposed gear.",
            ],
            "winter": [
                "Rime granules scrape across stone and fabric stiffens in minutes.",
            ],
            "storm": [
                "Blowing snow flattens the horizon and turns direction into a careful guess.",
            ],
        },
    },
    {
        "name": "Mossmere Wetlands",
        "terrain": "Boggy marsh",
        "flavor": "Peat-rich lowland spreads into shallow channels and standing pools, with ground firmness changing within a single stride. Sedge hummocks, cattail stands, and moss mats create a patchwork of support points above saturated soil. Organic sediment stains the water dark brown, and warm still pockets hold dense insect activity near dusk. Fallen trunks and root mats can serve as crossings, though each one is an experiment until tested. Morning fog sits close to the water surface and carries tannin and anaerobic mud notes. Animal sign is frequent at the marsh edge where firmer ground meets open water.",
        "gatherables": ["fiber", "berries", "mushroom"],
        "huntables": ["duck", "deer", "hare"],
        "water_sources": [
            {
                "name": "Reedwater",
                "quality": "murky",
                "description": "Still water among reed roots carries suspended peat particles and visible organic stain. Odor and turbidity increase in hot, windless periods.",
            },
            {
                "name": "Sprite Spring",
                "quality": "clear",
                "description": "A small upwelling pushes cool water through gravel, reducing sediment near the source. Surface insects concentrate at calm twilight and can foul shallow scoops.",
            },
        ],
        "pois": [
            {
                "name": "Singing Bog",
                "description": "Gas release through saturated peat creates periodic bubbling tones and ringed disturbance on shallow pools. Subsurface voids nearby can fail under concentrated weight.",
            },
            {
                "name": "Lantern Stumps",
                "description": "Waterlogged stumps host bioluminescent fungal bands that emit a steady green glow in low light. The glow is useful for orientation and not bright enough to ruin night vision.",
            },
        ],
        "temp_bias": 0,
        "resource_nodes": {
            "fiber": {"max": 9, "count": 7, "regen": 2},
            "berries": {"max": 6, "count": 4, "regen": 1},
            "mushroom": {"max": 8, "count": 6, "regen": 2},
        },
        "soundscape": {
            "day": [
                "Reed stems rattle in crosswind while insects hold a near-continuous drone.",
                "Mud vents release slow bubbles with soft popping near warm shallows.",
            ],
            "night": [
                "Frog calls layer across open pools in uneven intervals.",
            ],
            "winter": [
                "Thin edge ice tings against stems as water continues beneath.",
            ],
            "storm": [
                "Rain links isolated pools into broad shallow sheets over peat.",
            ],
        },
    },
    {
        "name": "Starfall Coast",
        "terrain": "Rocky coastline",
        "flavor": "Basalt shelves step toward surf under persistent wind, and spray leaves salt film on exposed surfaces within minutes. Coarse sand and rounded cobble gather between rock ribs, while barnacle bands mark recent tide reach. Dark algae on wet stone sharply reduces traction and forces slower, deliberate movement. Tidal timing controls route safety as much as terrain does, especially near cave mouths and low benches. Air carries salt and iron notes, and visibility near cliffs can fluctuate with spray drift. In clear dark conditions, wave-disturbed films may show faint blue phosphorescence along the waterline.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["crab", "seal", "fox"],
        "water_sources": [
            {
                "name": "Rain Cistern",
                "quality": "clean",
                "description": "A sheltered rock basin stores recent rainfall with generally low salinity when replenished. Windblown grit settles quickly and is easiest to avoid by drawing from deeper center water.",
            },
            {
                "name": "Cliff Seep",
                "quality": "salty",
                "description": "A thin seep crosses salt-crusted stone near spray exposure and tastes distinctly brackish. Salinity rises during heavy surf or onshore wind.",
            },
        ],
        "pois": [
            {
                "name": "Tide Caves",
                "description": "Wave-cut basalt chambers hold smooth runnels and narrow entrances that can close quickly with rising tide. Wet walls sometimes show faint bioluminescent films where foam repeatedly disturbs the surface.",
            },
            {
                "name": "Comet Watch",
                "description": "An exposed promontory offers a long horizon for weather reading and night sky observation. Wind load is persistent, and any open fire there demands careful shielding.",
            },
        ],
        "temp_bias": 1,
        "resource_nodes": {
            "stone": {"max": 10, "count": 8, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Wave backwash drags gravel in a coarse, rhythmic rattle.",
                "Spray strikes cliff faces in short bursts, then falls to hiss.",
            ],
            "night": [
                "Sets arrive in long intervals and cave mouths breathe with pressure change.",
            ],
            "winter": [
                "Cold spray drifts inland and leaves crust where droplets dry.",
            ],
            "storm": [
                "Heavy surf impacts the shelves and retreats with a deep stone-grinding pull.",
            ],
        },
    },
    {
        "name": "Pinewood Edge",
        "terrain": "Forest-meadow transition",
        "flavor": "Closed conifer canopy opens into grassland bands where solar heating changes quickly through the day. Soil transitions from needle-rich acidic duff to mixed loam with herb growth and patchy wildflowers. This edge habitat supports repeated crossing tracks from grazers and small predators, especially near dawn and evening. Movement is generally easier than deep forest, though root lines and shaded mud remain ankle hazards. Wind is stronger here than under full canopy and helps carry scent and distant calls. It is the kind of place where you can see more and still miss what is standing still.",
        "gatherables": ["stick", "fiber", "berries", "mushroom"],
        "huntables": ["hare", "deer", "fox"],
        "water_sources": [
            {
                "name": "Edge Run",
                "quality": "clear",
                "description": "A shallow stream leaves the woods with moderate flow over pebble substrate. Clarity is usually high unless recent trampling disturbed the banks.",
            },
            {
                "name": "Field Swale",
                "quality": "clean",
                "description": "Seasonal low-ground pooling captures rain and overbank flow in grass depressions. It stays clearer during dry spells and clouds quickly after heavy use by wildlife.",
            },
        ],
        "pois": [
            {
                "name": "Split Treeline",
                "description": "A staggered line of older pines forms a dependable windbreak between open grass and forest interior.",
            },
            {
                "name": "Fox Tracks",
                "description": "Repeated prints and scat along the same corridor indicate regular predator movement through the edge zone.",
            },
        ],
        "temp_bias": 0,
        "resource_nodes": {
            "stick": {"max": 8, "count": 6, "regen": 2},
            "fiber": {"max": 8, "count": 6, "regen": 2},
            "berries": {"max": 7, "count": 5, "regen": 1},
            "mushroom": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Grass heads brush together while canopy noise fades behind you.",
            ],
            "night": [
                "Open ground carries hoof movement farther than it seems it should.",
            ],
            "winter": [
                "Frozen grass rasps lightly under shifting wind.",
            ],
            "storm": [
                "Rain crosses from treetops to open field in visible sheets.",
            ],
        },
    },
    {
        "name": "High Scrub",
        "terrain": "Canyon-tundra transition",
        "flavor": "Elevated benches of fractured red stone meet colder exposure and stronger wind than the lower canyon. Soil is thin and discontinuous, supporting low shrubs, hardy bunchgrass, and sparse seasonal forbs in protected pockets. Thermal contrast is sharp: sunlit rock can be warm while shaded cuts hold persistent chill. Loose talus interrupts direct travel and rewards contouring along stable ribs. Visibility is broad, but depth cues in heat shimmer and spindrift are not always trustworthy. Animal sign appears concentrated near brief seep lines and lee-side forage patches.",
        "gatherables": ["stone", "fiber", "stick"],
        "huntables": ["goat", "fox", "hare", "lizard"],
        "water_sources": [
            {
                "name": "Bench Seep",
                "quality": "risky",
                "description": "Intermittent seep water emerges along bedding planes with clear appearance but high mineral influence. Flow reliability drops rapidly after extended dry periods.",
            },
            {
                "name": "Snow Runnel",
                "quality": "cold",
                "description": "Seasonal meltwater follows shallow channels on shaded slopes and remains very cold even under clear sun.",
            },
        ],
        "pois": [
            {
                "name": "Wind Notch",
                "description": "A narrow saddle accelerates air movement and can produce abrupt wind-chill exposure during crossings.",
            },
            {
                "name": "Shard Flats",
                "description": "Broad fields of broken shale shift and click underfoot, signaling unstable footing before it gives way.",
            },
        ],
        "temp_bias": -2,
        "resource_nodes": {
            "stone": {"max": 9, "count": 7, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "stick": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Loose shale ticks downslope in short runs after gusts.",
            ],
            "night": [
                "Cold air funnels through cuts and leaves a long narrow tone.",
            ],
            "winter": [
                "Spindrift crosses exposed benches and gathers in low pockets.",
            ],
            "storm": [
                "Gust fronts push grit over stone in a dry continuous hiss.",
            ],
        },
    },
    {
        "name": "Reed Margin",
        "terrain": "Wetland-forest transition",
        "flavor": "This boundary zone mixes alder thickets, mossy logs, and open reed channels where water level controls travel options day to day. Peat and forest litter combine into soft, dark soil that records tracks clearly until the next rain. Young trees colonize slightly higher ground, while cattails and sedges dominate saturated depressions. Progress is possible with care, but probing unknown steps remains wise near dark water pockets. Fog lingers longest here at first light and lifts in strips as breeze enters from drier ground. It is productive country for foragers, mosquitoes, and anyone stubborn enough to keep moving.",
        "gatherables": ["fiber", "berries", "mushroom", "stick"],
        "huntables": ["duck", "deer", "hare", "boar"],
        "water_sources": [
            {
                "name": "Alder Flow",
                "quality": "clear",
                "description": "A slow stream passes through root tangles with moderate tannin tint but generally low suspended sediment. Channel depth varies quickly near logjams.",
            },
            {
                "name": "Backwater Pocket",
                "quality": "murky",
                "description": "A stagnant side basin accumulates organic fines and algae film during warm calm weather. Surface clarity can be misleadingly better than lower layers.",
            },
        ],
        "pois": [
            {
                "name": "Root Causeway",
                "description": "Interlocked roots create one of the few semi-reliable crossings over knee-deep mud and standing water.",
            },
            {
                "name": "Mist Lamp Fungus",
                "description": "Pale fungal mats on soaked bark emit a low steady glow in dark humid conditions, likely from persistent bioluminescent colonies.",
            },
        ],
        "temp_bias": -1,
        "resource_nodes": {
            "fiber": {"max": 9, "count": 7, "regen": 2},
            "berries": {"max": 6, "count": 4, "regen": 1},
            "mushroom": {"max": 7, "count": 5, "regen": 2},
            "stick": {"max": 7, "count": 5, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Water drips from alder roots while reed tops rattle in side wind.",
            ],
            "night": [
                "Frog calls taper into forest insect noise along the margin.",
            ],
            "winter": [
                "Thin ice rings against root channels where current still moves.",
            ],
            "storm": [
                "Overflow links side pools and turns footpaths into shallow flow.",
            ],
        },
    },
    {
        "name": "Pebble Strand",
        "terrain": "Coast-upland transition",
        "flavor": "A broad shingle slope rises from wave reach into low scrub and wind-shaped grass, connecting marine edge to drier upland. Rounded stones drain quickly but roll under load, forcing short deliberate steps when carrying weight. Driftwood and wrack lines mark recent water heights and help read storm history at a glance. Salt exposure decreases with elevation, and plant cover increases in small protected hollows. Wind remains persistent but less punishing than cliff promontories farther out. It is a practical place to observe weather change if you do not mind getting reminded that pebbles move more than they look.",
        "gatherables": ["stone", "fiber", "stick", "berries"],
        "huntables": ["crab", "fox", "deer"],
        "water_sources": [
            {
                "name": "Drift Basin",
                "quality": "clean",
                "description": "Rainwater collects behind driftwood berms and can remain fresh between high-spray events. Windblown sand is the main visible contaminant.",
            },
            {
                "name": "Foam Sluice",
                "quality": "salty",
                "description": "A shallow runnel fed by wave splash carries brackish water and fine suspended sand, especially on rising tide.",
            },
        ],
        "pois": [
            {
                "name": "Shingle Fan",
                "description": "A wide fan of graded pebbles records storm energy through grain sorting and crest height.",
            },
            {
                "name": "Windbreak Bluff",
                "description": "A low bluff provides partial lee shelter above spray line, useful for maintaining controlled flame.",
            },
        ],
        "temp_bias": 1,
        "resource_nodes": {
            "stone": {"max": 9, "count": 7, "regen": 2},
            "fiber": {"max": 6, "count": 4, "regen": 1},
            "stick": {"max": 6, "count": 4, "regen": 1},
            "berries": {"max": 5, "count": 3, "regen": 1},
        },
        "soundscape": {
            "day": [
                "Retreating waves roll pebbles in a coarse, even cadence.",
            ],
            "night": [
                "Long-interval sets arrive from offshore and fade under upland grass noise.",
            ],
            "winter": [
                "Fine spray drifts inland and dries into a granular salt trace.",
            ],
            "storm": [
                "Breaking sets strike the upper strand and rattle stone downslope.",
            ],
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
        "mood": "High visibility follows thin cloud cover and weak pressure gradients, with light surface wind and stable air through most of the day. Shadows hold clear edges, and radiant cooling becomes noticeable soon after sunset on exposed ground.",
    },
    {
        "name": "Rain",
        "temperature_shift": -2,
        "thirst_rate": -1,
        "fire_modifier": -0.15,
        "hunt_modifier": -0.05,
        "mood": "Low stratiform cloud, elevated humidity, and sustained precipitation reduce distance contrast and damp most fuel surfaces. Wind is usually moderate but persistent, and water films quickly change traction on wood, stone, and soil.",
    },
    {
        "name": "Storm",
        "temperature_shift": -4,
        "thirst_rate": 1,
        "fire_modifier": -0.35,
        "hunt_modifier": -0.2,
        "mood": "Cumulonimbus build-up, gust fronts, and rapid pressure shifts mark unstable air and short decision windows. Heavy rain and strong wind bursts sharply reduce visibility, and thunder reverberation can obscure true distance to active cells.",
    },
    {
        "name": "Heatwave",
        "temperature_shift": 4,
        "thirst_rate": 2,
        "fire_modifier": 0.1,
        "hunt_modifier": -0.1,
        "mood": "A broad high-pressure pattern drives hot, dry air and sustained solar loading across exposed terrain. Heat shimmer increases, surface moisture drops quickly, and dehydration risk rises even at moderate activity levels.",
    },
    {
        "name": "Frostwind",
        "temperature_shift": -6,
        "thirst_rate": 1,
        "fire_modifier": 0.2,
        "hunt_modifier": -0.05,
        "mood": "Strong cold advection lowers skin temperature rapidly, with fine ice grains carried in persistent gusts. Visibility may remain good, but wind chill pushes safe exposure times downward and makes manual tasks slower.",
    },
    {
        "name": "Fairy Mist",
        "temperature_shift": -1,
        "thirst_rate": 0,
        "fire_modifier": 0.05,
        "hunt_modifier": 0.1,
        "mood": "Moist near-surface air condenses into low fog bands that narrow sightlines and mute distant contrast. A faint ozone-sweet note often accompanies this pattern, and occasional distant points of light are observable through shifting droplets, likely insects or reflective moisture effects.",
    },
]

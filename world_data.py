"""Static world and weather data for Campfire Cantos."""

WORLD_DATA = [
    {
        "name": "Emerald Pinewood",
        "terrain": "Dense conifer forest",
        "flavor": "Tall pines stand in close ranks, and their trunks push the wind into a low, steady hush that carries far between them. | Needle litter, moss pads, and old cones blanket the ground between root flares, while fir sap and damp bark give the air a resin-heavy scent near broken limbs. Fern pockets and berry thickets cluster where light reaches the understory, and fallen logs draw narrow green lines of lichen down their sides. | Footing alternates between springy duff and slick wood; progress is easy until you step onto bark polished by rain or moss, then suddenly less elegant. Small runoff channels hide under needles, so ankles can surprise you if you travel fast with a full pack. Animal tracks are common near soft banks, especially where game trails cross shallow water. | Light filters in layered bands through the canopy, leaving bright columns beside deep shade, and visibility tightens to short corridors once mist settles at branch height.",
        "gatherables": ["stick", "fiber", "mushroom", "berries"],
        "huntables": ["hare", "boar"],
        "water_sources": [
            {
                "name": "Needlebrook",
                "quality": "clear",
                "description": "Cold, fast water threads over visible gravel and rounded stone, and the current keeps sediment low except after heavy rain. Root mats narrow parts of the channel, making good fill points where the flow folds into small, oxygen-rich riffles.",
            },
            {
                "name": "Dew Pools",
                "quality": "clean",
                "description": "Shallow pools collect in shaded depressions after cool nights, usually clear at first light with only light plant debris on the surface. Water quality is best when skimmed above leaf litter and before midday insects begin to cluster.",
            },
        ],
        "pois": [
            {
                "name": "Whisperfall",
                "description": "A narrow ribbon of water drops over dark basalt into a compact plunge basin ringed by wet stone. The constant fall noise masks nearby movement, which helps with concealment but also hides approaching steps. Fine spray keeps surrounding rock slick, and footing improves a few paces back from the edge.",
            },
            {
                "name": "Moonroot Hollow",
                "description": "This shallow root-bound cavity opens beneath an upturned pine where soil has washed out over time. After dusk, thin root fibers show a faint silver glow that remains steady for minutes at a stretch, with no obvious source beyond the roots themselves. The chamber stays dry in light rain and breaks wind well enough for a short rest.",
            },
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
        "flavor": "Red sandstone walls rise in long, broken tiers that hold heat well into evening and throw back even quiet sounds. | Sparse scrub clings to ledges, while canyon floors mix coarse sand, shale chips, and pale talus fans where cliffs shed stone. Mineral streaks run down the rock faces in iron and chalk tones, giving clear clues about old water paths and seep lines. | Travel is direct on packed sand but unstable on loose scree; each step on steep talus asks for patience and careful weight shifts. Dry gullies can be safe one hour and flash channels the next, especially after distant storms. Shade is patchy at midday, and route choices matter more than speed when the rock starts radiating heat. | Air often carries a dusty mineral taste, and heat haze trembles above open stone, softening distant edges until landmarks appear to drift.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["lizard", "goat"],
        "water_sources": [
            {
                "name": "Dripstone Basin",
                "quality": "risky",
                "description": "Slow cave drips gather in a mineral-lined bowl where the water looks clear but leaves a metallic trace on the tongue. The basin can be useful in dry spells, though dissolved minerals and stagnant edges make treatment the safer choice.",
            },
            {
                "name": "Flash Creek",
                "quality": "muddy",
                "description": "When rain hits upstream, this channel appears quickly and carries suspended silt that turns the flow opaque brown. Sediment settles after several hours of calm, but the bed remains unstable and easy to undercut near bends.",
            },
        ],
        "pois": [
            {
                "name": "Echo Arch",
                "description": "A freestanding stone span bridges a narrow gap where sound reflects with unusual clarity. Short calls return in distinct beats, and longer speech comes back clipped and reshaped by the curve of the arch. If you pause, you can count the delay and gauge distance to the far wall, which is mildly useful and mildly unsettling.",
            },
            {
                "name": "Skytooth Overlook",
                "description": "A thin ledge of fractured sandstone projects above the drainage network with broad views across side gullies. From here, flood scars, debris lines, and safe contour routes are easy to map before committing to a descent. Wind exposure is high, and loose rock at the approach rewards slow feet.",
            },
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
        "flavor": "Open ground stretches under a wide sky where wind crosses without much to slow it, carrying dry ice grains in constant motion. | Snow crust, exposed gravel, and low lichen mats define the surface, with only scattered dwarf shrubs offering sparse cover near shallow dips. Ice-polished stones reflect hard light during clear hours, and rime collects on any edge that faces prevailing gusts. | Walking is efficient on firm crust until it breaks, then each step can drop to uneven sublayers that twist ankles and steal warmth. Drifts hide shallow hollows and refrozen runnels, so route-finding depends on reading texture and wind pattern, not just distance. Shelter options are limited and usually low, forcing short work periods between warm-ups. | Visibility runs very long in clear weather, but spindrift can sweep through in bands that erase detail and flatten the horizon within minutes.",
        "gatherables": ["stick", "fiber", "mushroom"],
        "huntables": ["elk", "fox"],
        "water_sources": [
            {
                "name": "Melt Rill",
                "quality": "cold",
                "description": "A narrow run of meltwater threads out from blue ice and stays near freezing even under sun. The flow is usually clear, though slush crystals collect at edges and can block easy filling points.",
            },
            {
                "name": "Ice Lens",
                "quality": "clean",
                "description": "Clear water pools in a shallow ice pocket with little visible sediment and a crisp mineral taste. It remains reliable in daylight, then skins over rapidly once temperature drops.",
            },
        ],
        "pois": [
            {
                "name": "Aurora Spire",
                "description": "A jagged tower of dark stone rises from the plain and gathers thick rime on its windward face. On clear nights, faint moving lights are often seen above or behind the spire, shifting too slowly to be drifting sparks and too steadily to be easy to name. The base provides limited lee shelter if you stay clear of falling ice plates.",
            },
            {
                "name": "Howl Cavern",
                "description": "This ice-cut chamber narrows into slots that channel gusts into a long, resonant tone. Pitch changes with wind direction, which can serve as a rough cue for incoming weather shifts. Interior surfaces are slick and brittle, so the safest path stays near the textured outer wall.",
            },
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
        "flavor": "Wide peat flats and reed channels spread across low ground, with water sitting at or just below the surface in most directions. | Sedge hummocks, cattails, and moss mats break up open pools, while dark organic mud records tracks clearly and holds them for hours. Fallen branches sink partway into the muck and mark old crossings that may still hold weight if tested first. | Travel is slow through ankle- to calf-deep mud, and footing shifts from firm hummocks to sudden soft pockets with little warning. Slick roots and floating vegetation can hide holes, so probing ahead with a stick saves trouble. Insect density rises sharply near still water at dusk, and exposed skin pays the bill. | Morning fog hangs low over the channels, muting distance and carrying wet-earth and tannin odors long before open water comes into view.",
        "gatherables": ["fiber", "berries", "mushroom"],
        "huntables": ["duck", "deer"],
        "water_sources": [
            {
                "name": "Reedwater",
                "quality": "murky",
                "description": "Still brown water sits among reed roots with visible plant fines and peat suspended through the column. Tannin stain is strong, and a mild algae odor thickens along warm, windless edges.",
            },
            {
                "name": "Sprite Spring",
                "quality": "clear",
                "description": "A gravel upwelling pushes cool, clear water through a narrow vent and keeps sediment low near the source. Surface insects gather heavily in calm weather, so drawing from the center flow works best.",
            },
        ],
        "pois": [
            {
                "name": "Singing Bog",
                "description": "Gas vents release through saturated peat in periodic pulses, creating low tones and bubbling rings across shallow pools. Ground near active vents can collapse under concentrated weight, especially after rain. The sound carries far in fog and can help orient you, provided you remember that direction and solid footing are separate problems.",
            },
            {
                "name": "Lantern Stumps",
                "description": "A cluster of waterlogged stumps supports bands of bioluminescent fungus that emit a steady green glow after dark. The light is bright enough to mark a route edge without spoiling night vision, which feels generous for a swamp. In damp wind, the glow softens but remains visible from surprising distance.",
            },
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
        "flavor": "Black basalt cliffs step down toward the sea in broken shelves where swell and wind shape everything to a hard edge. | Coarse sand, tide wrack, and salt-tolerant grasses collect in pockets between rock ribs, while darker stone stays slick with algae near the high-water line. Barnacle bands and salt crust mark recent spray reach and help read safe paths across the platform. | Travel is straightforward on dry upper shelves but risky on wet basalt where thin algae film behaves like oil under boots. Incoming tide can cut off easy exits at cave mouths and narrow channels, so timing matters as much as footing. Wind loads increase near headlands and can shift balance when carrying gear or fire supplies. | Air tastes of salt and iron, and moving spray veils the cliff base in bright, shifting mist that reduces detail at a distance.",
        "gatherables": ["stone", "fiber", "berries"],
        "huntables": ["crab", "seal"],
        "water_sources": [
            {
                "name": "Rain Cistern",
                "quality": "clean",
                "description": "A sheltered basin in the rock collects recent rainfall and usually runs clear when inflow is fresh. Wind-blown grit can settle along one side, so cleaner draws come from the deeper center.",
            },
            {
                "name": "Cliff Seep",
                "quality": "salty",
                "description": "A thin seep crosses salt-crusted stone near constant spray and carries a distinct brackish taste. Salinity increases during rough surf, leaving white residue on containers as it dries.",
            },
        ],
        "pois": [
            {
                "name": "Tide Caves",
                "description": "Basalt sea caves open along the lower wall where waves have carved narrow chambers and smooth runnels. At night, wet surfaces sometimes show faint blue bioluminescent films that brighten when disturbed by foam. Access windows are short around rising tide, and retreat routes should be checked before entering.",
            },
            {
                "name": "Comet Watch",
                "description": "An exposed promontory extends past the cliff line and offers a broad horizon with minimal inland light obstruction. It is excellent for tracking meteor trails and weather fronts, though strong crosswinds make unshielded fires unreliable. If you stay long enough, the sky tends to provide either wonder or humility, occasionally both.",
            },
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

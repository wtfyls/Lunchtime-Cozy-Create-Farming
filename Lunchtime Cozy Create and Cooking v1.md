# Lunchtime — Performance, Progression & Exploration Overhaul

Lunchtime is receiving a major overhaul focused on performance, cozy building, deeper exploration, more intentional crafting progression, and better multiplayer gameplay.

This update expands the pack's questing, jobs, world generation, cooking, decoration, and exploration systems while reviewing overlapping features, unnecessary complexity, and potential compatibility issues.

## ⚡ Performance & Stability

• **Added Concurrent Chunk Management Engine (C2ME Forge).** Improves chunk-generation and chunk-loading workloads by allowing parts of the chunk pipeline to run concurrently. This is particularly relevant when exploring new terrain or generating a world with several biome and structure mods. Actual performance depends on the hardware and the compatibility of the installed world-generation mods.

• **Added additional performance utilities.** Fast Noise Mod targets world-generation performance, while Fast Item Frames focuses on item-frame overhead. FastALI, Fastvancements, Fast Suite, Async Logger, AsyncParticles, and More Culling expand the optimization stack across different systems.

• **Updated ModernFix and supporting libraries.** Keeps the pack's optimization and compatibility infrastructure current with the selected mod versions.

• **Added SparseStructures and NoStructureOverlap.** Gives us more control over how frequently structures appear and helps reduce unwanted structure collisions. The goal is to make exploration feel more intentional without filling every region with competing points of interest.

• **Reviewed performance-related configuration.** Continued checking world-generation density, client rendering, and server stability so the pack remains enjoyable on a wider range of systems.

These additions are intended to improve performance, but they are not a guarantee of higher FPS or lower server tick times on every setup. Compatibility and actual results still need to be evaluated in the complete pack.

## 📖 Quests & Progression

• **Added FTB Quests and FTB Quests UI Overhaul.** Provides a dedicated progression system for introducing players to the pack, explaining its major mods, and giving multiplayer groups shared goals beyond ordinary survival.

• **Added a custom welcome screen and quest artwork.** Gives new players a clearer introduction to Lunchtime and makes the quest interface feel more connected to the pack's identity.

• **Expanded the quest-reward possibilities.** Plushie Buddies are intended to serve as collectible rewards, giving players something to work toward rather than making every collectible an ordinary craftable item.

• **Added an extremely rare Star Wars-themed reward to the reward-table setup.** Intended as a special discovery rather than a routine reward. Its final rarity and availability depend on the reward configuration.

• **Expanded the recipe-viewing setup with EMI and supporting integrations.** EMI provides recipe lookup, searching, favorites, and recipe-tree features that can help players understand the ingredients and steps required for more complex crafts. Create EMI integrations further connect that experience to Create-related recipes and schematics.

• **Continued refining progression clarity.** The aim is to make it easier to discover what a mod does, understand crafting requirements, and decide what to work toward next.

## ⚒️ Crafting, Recipes & Automation

• **Rebalanced Easy Villagers and reviewed its farm progression.** The goal is to keep villager-based automation useful without allowing it to bypass too much of the intended survival progression. The related farm setup also needs to be tested in the finished pack.

• **Corrected the Waystone crafting recipe.** Makes the intended travel system's crafting progression more consistent with the pack's balance.

• **Rebalanced aircraft recipes.** Keeps aircraft progression within the broader survival and resource-gathering experience instead of making transportation feel disconnected from the rest of the pack.

• **Added Create EMI Compat, Create: EMI Schematics, and additional recipe integrations.** Improves the connection between recipe lookup and Create's mechanical crafting systems, helping players understand the components needed for larger contraptions.

• **Added Item Obliterator.** Allows selected items to be disabled through configuration. This is useful for removing items that duplicate another mod's role, do not fit the pack's intended progression, or create unwanted recipe and gameplay overlap. The exact disabled items depend on Lunchtime's configuration.

• **Continued reviewing overlapping mechanics.** The objective is not to remove every alternative system, but to give each major mechanic a clear purpose. Farming, cooking, transportation, storage, and Create automation should complement each other rather than compete unnecessarily.

## 💼 Jobs & Player Economy

• **Added Jobs+ and Jobs+ Tools.** Introduces profession-based progression that rewards players for performing different activities instead of relying exclusively on conventional mining and crafting.

• **Expanded the professions available to players.** The listed professions include Alchemist, Builder, Digger, Enchanter, Farmer, Fisherman, Hunter, Lumberjack, Miner, and Smith.

• **Added Shoppy.** Creates more opportunities for player-run shops and trading. Together with Jobs+, this gives multiplayer groups more reasons to specialize, exchange resources, and build an economy around their activities.

• **Designed around cooperative play.** Players can focus on different activities and trade what they gather or produce, rather than everyone needing to progress through every profession independently.

• **Additional custom professions may need further work.** Roles such as bard or bartender are ideas for future configuration or development, not confirmed finished features.

## 🌍 World Generation & Exploration

• **Added Integrated Dungeons and Structures, Integrated Villages, Moog's Mineshafts Reimagined, Moog's Temples Reimagined, and Moog's End Structures.** Expands the variety of locations players can discover and gives exploration more opportunities for unusual layouts, encounters, and rewards.

• **Added Luki's Woodland Mansions.** Expands the woodland-mansion exploration experience with additional structure content.

• **Added Regions Unexplored.** Introduces additional biome variety, giving players more environments to discover and more visual diversity across the world.

• **Added SparseStructures and NoStructureOverlap.** Supports a more controlled distribution of generated structures. This matters in a pack with multiple structure mods, where too many generation systems can compete for the same terrain.

• **Reviewed the existing structure lineup.** Several older YUNG's structure modules were removed from the supplied new mod list while selected modules were retained. The intent is to curate the overall structure selection rather than simply stack every available structure overhaul.

• **Continued configuring vanilla structure generation.** Selected vanilla structures are being disabled where they conflict with the intended structure lineup or are replaced by alternatives. The exact structures affected depend on the final configuration.

• **Recommended a fresh world for the best experience.** Because the biome and structure selection has changed, a new world is the safest way to experience the intended generation setup. Back up existing worlds before updating; do not delete your existing saves.

## 🍂 Seasons, Rivers & Underground Exploration

• **Added Ecliptic Seasons and its selected integrations.** Introduces seasonal changes to the world, making the environment feel less static and adding another layer to the cozy outdoor experience.

• **Added BetterDays.** Expands the pack's environmental and time-related atmosphere alongside the seasonal direction.

• **Added StreamsReflowing alongside RiverRedux.** Refreshes the river experience and helps make outdoor exploration and the landscapes around player builds feel more distinctive.

• **Added Spelunkery.** Expands underground exploration and mining content, giving caves and subterranean trips more variety.

• **Added Icy's Better Horses.** Improves the horse experience, supporting a more enjoyable way to travel through the world without relying exclusively on teleportation.

• **Continued refining environmental content.** Seasons, rivers, caves, and travel are intended to complement the pack's exploration and building systems rather than overwhelm the cozy atmosphere.

## 🏡 Cozy Building & Decoration

• **Added Another Furniture, Cozy Home, Cozy Cafe, Dusty Decorations, and Building But Better.** Expands the options for furnishing houses, designing cafés, decorating interiors, and adding detail to builds.

• **Removed Let's Do Furniture from the supplied new mod list.** The building lineup was being reorganized around the remaining decoration and furniture options, with the aim of reducing overlap and keeping the available building palette more intentional.

• **Retained established building options.** Mods such as Chipped, Decorative Blocks, Supplementaries, and Immersive Paintings continue to provide a broad selection of decorative blocks, functional details, and creative possibilities.

• **Added Plushie Buddies.** Supports the collectible-decoration direction, with plushies intended to become special quest rewards rather than ordinary craftable items.

• **Reviewed Quark's decorative content.** Selected blocks, palettes, and variants were disabled where they overlap with other building mods or do not fit the intended selection. This keeps the pack's large building palette easier to navigate.

• **Focused on practical creative freedom.** The aim is to provide plenty of ways to build cozy homes, kitchens, cafés, farms, and shared community spaces without adding every possible decorative variant.

## 🍳 Cooking, Farming & Food

• **Added Barbeque's Delight, Brewin' And Chewin', Butchery, Fishermens Trap, Simple Ice Cream, and Kaleidoscope Grilling.** Expands the ways players can prepare food, process ingredients, fish, and build more specialized kitchens.

• **Removed Ender's Delight from the supplied new mod list.** Keeps the food selection focused on the pack's main cooking and farming experience rather than retaining every optional food expansion.

• **Removed Let's Do Brewery, Let's Do Camping, and Let's Do HerbalBrews from the supplied new mod list.** These mods each add their own mechanics—for example, Brewery adds brewing, Camping adds outdoor equipment and campsite features, and HerbalBrews adds tea and coffee preparation. The revised selection prioritizes the cooking, farming, and decoration systems chosen for this version. This is a content-curation decision; it should not be interpreted as a confirmed incompatibility with those mods.

• **Retained the core Farmer's Delight ecosystem.** Existing additions such as Cultural Delights, Delightful, Alex's Delight, and Chef's Delight continue to expand the food options available to players.

• **Continued reviewing food consistency.** Ingredient unification and recipe review remain important goals: where possible, common ingredients such as tomatoes and onions should use a consistent item rather than several nearly identical versions from different mods.

• **Kept cooking central to the pack.** The objective is to make growing ingredients, gathering resources, preparing meals, and sharing food meaningful parts of everyday survival and multiplayer play.

## 🐾 Mobs, Encounters & Additional Content

• **Added Critters and Companions, Creeper Overhaul, Enderman Overhaul, Faunify, and Golem Overhaul.** Expands creature variety and adds more character to the world beyond the standard vanilla mob selection.

• **Added Cataclysm, Bosses'Rise, Combat Roll, DragonLoot, and It Takes A Pillage.** Expands combat encounters, boss-related content, movement options, loot, and hostile structures.

• **Reviewed creature spawn balance.** Mob variety should make the world feel alive without flooding players' bases or placing unnecessary pressure on lower-end clients and multiplayer servers.

• **Kept combat as an additional activity.** Lunchtime remains centered on building, farming, cooking, Create automation, and exploration. More dangerous encounters add variety without changing the entire pack into a combat-focused experience.

## 🎨 Interface, Audio & Multiplayer

• **Added ImmersiveUI, Inventory Particles, Chat Heads, ChatAnimation, ExtraSounds Next, Minecraft Cursor, and Emotecraft.** Expands the visual feedback, chat presentation, cursor customization, and emote options available to players.

• **Added Chat Heads Figura Support.** Provides a compatibility layer for the selected Chat Heads and Figura setup.

• **Added Exposure Polaroid and EMF Compat: Core.** Expands the photography setup and its related compatibility support.

• **Added e4all and additional FTB multiplayer tools.** Supports a more connected multiplayer experience and expands the utility available to players.

• **Reviewed keybinds and interface conflicts.** Optional controls should not unexpectedly override important keys or interfere with commonly used actions. Selected Quark controls and client conveniences are being disabled where they conflict with the intended control layout.

• **Continued reviewing the Escape menu and default settings.** The menu layout, resource-pack presentation, and exported defaults need to be consistent so players receive the intended setup when installing the pack. The final export should not rely on distributing a developer's personal `options.txt`.

• **Reviewed audio configuration.** Selected sounds and volume levels are being checked to reduce intrusive or unintended audio behavior.

• **Retained Simple Voice Chat, Waystones, Xaero's Minimap, and Xaero's World Map.** These continue to support communication, navigation, and multiplayer exploration.

## ⚙️ Quark Configuration Overhaul

Quark includes a wide range of optional features. Rather than enabling everything by default, Lunchtime's configuration is being curated to reduce overlap with other mods and keep the gameplay consistent.

• **Automation:** Selected features such as Chute, Gravisand, Iron Rod, and Redstone Randomizer are disabled to reduce unwanted alternative automation options.

• **Building and decoration:** Selected blocks, palettes, lamps, glass options, posts, slabs, ropes, and decorative variants are disabled where they overlap with the pack's existing building selection.

• **Inventory management:** Easy Transferring, Expanded Item Interactions, Hotbar Changer, and Inventory Sorting are disabled to avoid duplicating inventory conveniences or introducing unwanted behavior.

• **Tools and gameplay tweaks:** Selected features such as Pickarang, Pathfinder Maps, Torch Arrows, Automatic Recipe Unlock, and other optional mechanics are disabled to keep progression and controls intentional.

• **World generation and mobs:** New Stone Types, No More Lava Pockets, Permafrost, and Crabs are among the selected features marked for disabling, helping keep the world-generation and creature selection aligned with the rest of the pack.

• **Client features:** Selected options such as Auto Walk, Camera Mode, Chest Searching, Greener Grass, and Microcraft Helper are marked for disabling to reduce unwanted controls, visual distractions, or duplicated conveniences.

• **Experimental features:** The configuration plan is to disable all Quark Experimental options unless a specific feature is deliberately chosen and tested.

The goal is not to suggest that these Quark features are inherently broken. It is to choose which features belong in Lunchtime and avoid adding multiple systems that do the same job.

## 🧹 Mod Removals & Compatibility Decisions

• **Tom's Simple Storage — removed.** Create already provides the pack's central automation and logistics gameplay. Tom's Simple Storage adds its own storage terminals, inventory connectors, and related systems, which would introduce another storage workflow alongside Create. During Lunchtime development, the mod also presented a Create-related conflict. Removing it avoids maintaining two overlapping approaches to storage and automation and keeps the pack's progression more focused on Create.

• **Let's Do Furniture — removed from the new mod list.** The decoration selection was reorganized around the remaining furniture and building mods. The aim is to maintain a broad creative palette while avoiding unnecessary overlap.

• **Ender's Delight — removed from the new mod list.** The food selection was streamlined around the pack's main cooking and farming systems.

• **Let's Do Brewery, Camping, and HerbalBrews — removed from the new mod list.** These add separate brewing, campsite, and tea/coffee systems. The revised selection prioritizes the cooking and building systems chosen for this version rather than keeping every optional side system.

• **Selected YUNG's structure modules — removed from the new mod list.** The structure lineup was curated alongside Moog's and Integrated Dungeons and Structures content. The goal is to reduce the number of overlapping structure systems and make loot and world-generation behavior easier to manage. This does not mean every YUNG's mod was removed.

• **Continuity — absent from the supplied new mod list.** Continuity provides connected-texture support for compatible resource packs, but the exact reason for its omission has not been documented in the change notes. It should not be described as a confirmed conflict or bug without the relevant testing details.

• **Other optional content — curated rather than automatically retained.** The mod list was reviewed to prioritize compatibility, performance, a cohesive cozy theme, and clear progression. Individual removal reasons should only be attributed to a specific bug or conflict when that issue was actually observed during development.

## 🧭 Travel & Community Play

• **Kept Waystones as the intended travel system.** The crafting recipe was corrected in development, and the server's travel commands are being reviewed so that players use the intended progression and permissions.

• **Retained multiplayer support through FTB Teams, FTB Chunks, Simple Voice Chat, and related tools.** These systems support shared bases, claims, communication, and coordinated progression.

• **Continued improving the shared experience.** The goal is to make Lunchtime work as a cozy single-player experience while also supporting groups that want to build, trade, explore, and progress together.

## 💚 The Direction for Lunchtime

This overhaul is about making Lunchtime feel more cohesive—not simply adding as many mods as possible.

Performance tools help support a larger experience. Quests give players direction. Jobs and shops create reasons to specialize and trade. New structures and biomes make exploration more rewarding. Cooking, furniture, and decoration keep the cozy identity at the center of the pack.

At the same time, removing overlapping systems and carefully configuring optional features helps keep the experience easier to understand and maintain.

**Lunchtime — a little more to explore, a little more to build, and a lot more to do together.**

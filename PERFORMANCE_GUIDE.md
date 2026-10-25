# Lunchtime Performance Guide

Lunchtime is a large Forge modpack for Minecraft 1.20.1. The supplied mod list contains **379 entries**, including content mods, world-generation mods, client visuals, performance tools, and shared libraries. That means performance depends on more than one setting: your hardware, RAM allocation, the world, what is loaded nearby, and whether you are playing single-player or on a dedicated server all matter.

This guide gives you a reliable starting point. The settings below are practical suggestions, not official minimum requirements or guaranteed FPS targets.

## Quick fixes first

If Lunchtime feels slow, try these in order:

1. **Let the first launch finish.** Large packs may take longer to initialize after an update. Avoid force-closing the game while it is still loading unless it is genuinely unresponsive.
2. **Use the correct Java version.** Minecraft 1.20.1 modpacks normally use a 64-bit Java 17 runtime. Let your launcher manage the bundled runtime when it offers a compatible one.
3. **Start with default Lunchtime settings.** Temporarily remove extra shaders, resource packs, or additional mods you added yourself when troubleshooting.
4. **Lower render and simulation distance.** Start at 8 chunks render distance and 5–6 chunks simulation distance. Raise them gradually if performance is good.
5. **Check what kind of lag you have.** Low FPS, slow chunk generation, and server tick lag are different problems. See [Diagnosing the problem](#diagnosing-the-problem).
6. **Don't blindly add optimization mods or JVM arguments.** Lunchtime already includes several optimization and diagnostic mods. Extra replacements may conflict with the pack.

## Client settings

These are good starting values for a mid-range or lower-end PC. Adjust one setting at a time so you can tell which change helped.

| Setting | Starting point | Why |
|---|---:|---|
| Render distance | 8 chunks | Fewer terrain sections to render |
| Simulation distance | 5–6 chunks | Fewer nearby chunks actively ticking |
| Entity distance | 50–75% | Reduces how far away entities are rendered |
| Particles | Decreased | Reduces particle workload in busy scenes |
| Graphics | Fast or Fancy, whichever performs better | Fancy effects can cost more on some systems |
| Clouds | Off, if needed | Removes a visual layer |
| Shaders | Off while troubleshooting | Shader packs can add substantial GPU load |
| High-resolution resource packs | Disable while testing | Large textures can increase VRAM and memory use |

For the fairest test, load the same world and stand in the same place before and after each change. Moving through a new area makes the game generate and load terrain, so it is not a clean FPS comparison.

## Memory and Java

### How much RAM should I allocate?

For this large pack, **8 GB is a reasonable starting point for the Minecraft client** on a computer with enough total memory. Some systems or sessions may need less or more; measure actual use before changing it. This is a practical starting suggestion, not a tested guarantee for every Lunchtime version.

- Do not allocate all system RAM to Minecraft. Your operating system, launcher, browser, voice chat, and other applications also need memory.
- Too little memory can cause repeated garbage collection, stutters, or crashes.
- More allocated RAM is not automatically better. Excessive allocation can leave too little memory for the rest of the computer and may not improve performance.
- Use your launcher's memory setting rather than copying a large bundle of Java flags from a random guide.
- If you change memory allocation, restart Minecraft completely before testing again.

For a dedicated server, choose memory based on player count, world-generation activity, view distance, loaded machines, and measured use. Don't assume that the client and server should receive the same allocation.

## Performance mods included in Lunchtime

The supplied list already includes a number of optimization and troubleshooting tools. Their exact effects depend on configuration, hardware, and compatibility; they do not eliminate the cost of every content or world-generation mod.

| Mod | Main purpose |
|---|---|
| **Embeddium** | Reworks client terrain rendering and optimizes rendering workloads. |
| **ModernFix** | A broad collection of performance, memory-use, loading, and bug-fix improvements. |
| **Ferrite Core** | Reduces memory use in supported game data structures. |
| **BadOptimizations** | Applies assorted client-side performance optimizations. |
| **Dynamic FPS** | Reduces resource use when Minecraft is unfocused or in the background. |
| **Entity Culling** | Skips rendering entities that are hidden from view. |
| **More Culling** | Avoids drawing certain block faces and other elements that cannot be seen. |
| **ImmediatelyFast** | Optimizes several immediate-mode rendering paths. Check the exact installed file's compatibility with the pack's Minecraft version. |
| **Fast Noise Mod** | Optimizes parts of vanilla world-generation noise calculations. |
| **Concurrent Chunk Management Engine (Forge)** | Attempts to improve chunk generation, loading, and I/O by doing more work concurrently. Custom world-generation mods can make compatibility testing especially important. |
| **Alternate Current** | Optimizes redstone wire updates. |
| **Radium** | Provides general game-logic optimizations derived from the Lithium project. |
| **FastBoot** | Targets startup/loading performance. |
| **FastFurnace, Fast Workbench, Fast Suite** | Optimize selected recipe, furnace, or crafting-related operations. |
| **Fast Item Frames, Fast Paintings** | Reduce overhead associated with supported item-frame and painting behavior. |
| **Fastvancements** | Optimizes advancement-related processing. |
| **Async Logger** | Moves supported logging work off the main execution path. |
| **AsyncParticles** | Changes how supported particle work is handled to reduce its impact. |
| **Mobtimizations** | Applies optimizations to mob/entity-related processing. |
| **Structure Layout Optimizer** | Optimizes aspects of structure placement/layout calculations. |
| **Chunky** | Lets server administrators pre-generate chunks before players explore them. |
| **spark** | Profiles CPU/tick activity so you can diagnose the actual source of lag. |

Some optimization tools target only the client, others the server, and some both. Don't copy every client-only mod into a dedicated server, and don't remove a mod from only one side if the pack expects it on both. Use the pack's official server files and instructions.

References: [Embeddium](https://modrinth.com/mod/embeddium), [ModernFix](https://modrinth.com/mod/modernfix), [Fast Noise](https://modrinth.com/project/OnlVIpq5), [C2ME for Forge](https://modrinth.com/mod/c2mef), and [spark command documentation](https://spark.lucko.me/docs/Commands).

## Dedicated server performance

If you host a Lunchtime server, these are reasonable **initial test values**, not mandatory settings:

- `view-distance=6` to `8`
- `simulation-distance=4` to `6`

Lower distances can reduce the amount of world and entity activity the server must handle. Increase them only after checking performance with your usual number of players and the areas they visit.

### Pre-generate terrain with Chunky

New terrain can cause temporary CPU and disk load, especially in modpacks with many biomes and structures. If you administer the server, pre-generate a sensible area before players explore it.

Example commands (run as a server operator; replace the center coordinates with your world spawn):

```text
/chunky center <spawnX> <spawnZ>
/chunky radius 3000
/chunky start
```

Pick a radius that fits your storage and server capacity. World generation is expensive, so do this during maintenance or while the server is empty. Back up important worlds before major world-generation changes.

### Profile the server instead of guessing

If the server has lag spikes or low TPS, use the included **spark** profiler while the problem is happening. For a server, run:

```text
/spark profiler start --timeout 120
```

Reproduce the lag for about two minutes and let the profiler finish. The resulting report can show which code paths are using tick time. If you need to stop early, use `/spark profiler stop`.

Low FPS on your own computer is not automatically a server problem. Likewise, a server can have healthy tick performance while one player's client renders slowly.

## Diagnose the symptom

### Low FPS, but the world runs at normal speed

- Lower render distance, entity distance, and particles.
- Disable shaders and high-resolution resource packs for a test.
- Close GPU-heavy apps and check that Minecraft is using the intended graphics processor.
- Check the GPU/VRAM and CPU load while the frame rate is low.
- Make sure the issue also happens with the unmodified Lunchtime instance.

### Stutters when exploring or generating chunks

- Reduce render distance temporarily.
- Test the area again after it has been generated once.
- On a server, consider controlled Chunky pre-generation.
- Give new world-generation changes extra compatibility testing. Concurrent chunk-generation optimizers can interact with custom biome and structure mods.

### Server lag, rubber-banding, or slow block/entity updates

- Check whether everyone is affected or only one player.
- Check server CPU, memory, storage, and network usage.
- Reduce server view and simulation distance for a controlled test.
- Run a spark profile during the lag rather than guessing which mod is responsible.
- Check whether large Create contraptions, many entities, hoppers, or active farms are involved.

### Crashes or long loading screens

- Check the crash report and `logs/latest.log`; look for the first meaningful error, not just the last line.
- Confirm you are running the supported Minecraft, Forge, Java, and Lunchtime versions together.
- Remove any extra mods you added yourself before reporting a pack issue.
- Don't delete worlds or randomly remove mods from an existing save. Back up the world first.

## Lunchtime-specific notes

Lunchtime contains extensive world-generation, structure, mob, Create, cooking, decoration, and recipe content. Exploring new terrain or loading a busy base can naturally cost more resources than standing still in an empty area. A performance mod may reduce a particular workload without making every situation faster.

The **1.5 hotfix removed Ecliptic Seasons and its add-ons because of excessive CPU usage**. If you are using a different pack version or a custom instance, its mod list may differ from the current release notes. Check the actual installed pack version before comparing results.

## When asking for help

Please include:

- Lunchtime version and launcher
- Minecraft/Forge version and Java version
- Whether you play single-player, host a world, or use a dedicated server
- Your CPU, GPU, and total system RAM
- Whether the problem is low FPS, chunk generation, server TPS, stutter, or a crash
- A relevant sanitized crash report, `latest.log`, or spark profile link

Remove passwords, access tokens, private IPs, and other sensitive information before sharing logs. A repeatable report helps us fix the cause instead of recommending random settings.

---

*This guide is a troubleshooting baseline, not a benchmark claim. Performance varies by hardware, world, configuration, and installed pack version.*

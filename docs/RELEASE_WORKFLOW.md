# Release workflow

This document is the standard process for every Lunchtime update.

## 1. Track changes while developing

Use GitHub Issues or the team's task board for work that needs discussion, testing, or assignment. For small changes, add a short bullet to the `Unreleased` section in `CHANGELOG.md`.

Use these categories:

- **Added** — new features, mods, quests, or content
- **Changed** — configuration, recipes, balance, keybinds, or behavior changes
- **Fixed** — bugs and compatibility problems resolved
- **Removed** — mods, content, or features removed
- **Performance** — significant performance work (use this when it deserves its own heading)
- **Known issues** — relevant problems still present in the release

Write the player-facing impact and the reason when useful. Avoid claiming performance improved unless testing supports that claim.

## 2. Prepare the release

1. Confirm the release version with the team.
2. Review the actual mod/config changes so notes describe what shipped, not just what was planned.
3. Test a clean client launch and a dedicated server launch when relevant.
4. Check world loading, multiplayer, important quests/recipes, and logs.
5. Move the finished changes from `Unreleased` into a new version section in `CHANGELOG.md`.
6. Create `docs/releases/<version>.md` only when a longer explanation, screenshots, or extra testing details are useful.
7. Write a concise CurseForge release description from the same verified changes.

## 3. Publish on GitHub

1. Commit the release notes to the default branch.
2. Create a Git tag matching the chosen version, such as `1.5` (use the exact version the team has agreed on).
3. Create a GitHub Release from that tag.
4. Use the matching section of `CHANGELOG.md` for the release description.
5. Link to the CurseForge release/download page. Do not upload the full assembled modpack to GitHub unless there's a deliberate, permitted reason.

## 4. Keep the version history consistent

- One published pack version should map to one Git tag and one GitHub Release.
- Keep the same version spelling on GitHub and CurseForge wherever practical.
- Do not silently rewrite an already-published release's notes; add a correction if needed.
- Keep `Unreleased` for work that has not shipped.
- Never describe a planned mod or feature as added until it is actually included in the release.

## 5. Screenshot and image guidance

Use screenshots that clearly show the feature being discussed. Store project-owned images under `assets/` and link them from Markdown, for example:

```md
![New build in Lunchtime](../assets/screenshots/new-build.png)
```

Use descriptive filenames such as `create-factory-before.png`, not `image1.png`. Only commit images you have permission to use, and credit third-party work where required.

# Los Santos: Mob War

**Status: source-only design scaffold — not a playable mod and not ready for Melty release.**

Los Santos: Mob War is a proposed co-op crossover with **Grand Theft Auto V Enhanced as the primary game** and **Minecraft: Java Edition as a companion game**. Release 1 prioritizes online co-op, Minecraft hostile mobs fighting GTA police, combat encounters, and cross-game explosion events. Block placement/destruction and Nether invasion events are deferred to a later update.

## Agreed direction

- **Primary:** GTA V Enhanced; preserve the player's GTA window and host game.
- **Companion:** Minecraft: Java Edition, using a Melty-managed Fabric instance if current catalog metadata confirms support.
- **First-minute scenario:** reach a Los Santos street, trigger a police-versus-mob encounter, then escalate into combat and explosions.
- **Multiplayer:** online co-op is a release-one requirement. Player capacity and internet reachability are unclaimed until tested.
- **Game assets:** read game-owned assets from each player's own installations. Do not bundle GTA or Minecraft game files, models, textures, audio, levels, or extracted content.
- **Safety:** never disable or bypass BattlEye. Do not depend on a manually installed Script Hook V. A GTA V Legacy prototype is not an acceptable replacement for Enhanced.

## Repository contents

- design/: JSON sheets for game roles, systems, entities, events, hooks, multiplayer, licensing decisions, and release preflight
- docs/network-protocol.md: proposed message envelope and multiplayer acceptance tests
- tools/validate_sheets.py: JSON syntax and cross-reference validation
- .github/workflows/validate-design.yml: runs the structural validator on push and pull requests
- MODLOG.md and REPOSITORY_STATUS.md: findings and unresolved blockers

## Not yet implemented

This repository does **not** include a GTA Enhanced ASI/plugin, Minecraft Fabric mod JAR, cross-game bridge, Melty multiplayer recipe, release archive, gameplay screenshot, or passing two-client test. Structural validation is not gameplay validation. Do not submit this scaffold as a playable release.

## Release gates

1. Run Melty's current game-info, mashup search, multiplayer setup, recipe validation, and one-click checks.
2. Inspect the actual Windows installs of GTA V Enhanced and Minecraft; install and follow universal-modder's mod-any-game skill.
3. Prove an Enhanced-compatible integration without disabling BattlEye or relying on manually installed loaders.
4. Implement the Fabric companion and a Melty-generated multiplayer configuration.
5. Build, preflight every sheet, package, capture real gameplay, and test with two clients launched through Melty.
6. Confirm credits, source license, and remix permissions before listing.
7. Ask for publishing approval only after the build and tests pass.

See design/preflight.json for the current blockers.

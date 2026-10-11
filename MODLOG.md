# MODLOG — Los Santos: Mob War

## 2026-10-11 — Design intake and initial preflight

### User-approved scope
- The two games interact in one crossover sandbox.
- GTA V Enhanced remains the primary game; Minecraft Java is the companion.
- Release 1 prioritizes online co-op combat, Minecraft mobs versus GTA police, and explosion events.
- The first-minute scenario starts in Los Santos, introduces a police-versus-mob encounter, and escalates combat/explosions.
- Full block building/destruction and Nether invasion events are deferred.

### Reference constraints
- The closest surfaced Melty listing is GTA IV in Minecraft; it is a different GTA title and not a ready-made implementation of this project.
- A community/reference GTA V crossover targets Legacy and relies on Script Hook V with BattlEye disabled. That setup is explicitly not reused here.
- Use Melty's game_info as the authority on supported routes and risks. Use universal-modder and its mod-any-game skill to inspect the actual installed game files once the development environment is available.

### Current execution limits
- This runtime does not expose a Windows development session with both game installations.
- No successful Melty MCP calls or Melty recipe/test results have been obtained from this environment.
- The source files are structural design only; no native component has been compiled, loaded, or played.
- No gameplay media was fabricated.

### Proposed route (unverified)
- Keep GTA V Enhanced as the Melty primary and Minecraft Java as companion.
- Investigate an Enhanced-compatible native ASI route via Melty-provided Ultimate ASI Loader; retain BattlEye and avoid manually installed Script Hook V.
- Use a Melty-managed Prism/Fabric Minecraft instance after confirming supported version metadata.
- Generate multiplayer wiring with Melty's setup_multiplayer rather than inventing a recipe or claiming NAT traversal.
- Read game content from each player's installed copy; do not bundle game assets.

### Next steps
1. Connect to Melty and call list_my_mods, search_mashups, game_info for both games, and mashup_info for the closest launched example.
2. Install/clone universal-modder and run its inspection workflow against the actual game installations.
3. Resolve all design-sheet blockers before build; do not mark unspecified implementation cells as complete.
4. Build the Enhanced and Fabric components and test host/join with two running clients and both logs.
5. Inspect every archive entry, validate recipe destinations, run one_click_check, capture genuine gameplay, test the Melty-installed release, and obtain approval before publishing.

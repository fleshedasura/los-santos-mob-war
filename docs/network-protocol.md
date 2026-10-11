# Cross-game multiplayer protocol (design contract)

This is a protocol draft, not implemented transport code. Messages are session-scoped and versioned. Use transport and multiplayer wiring produced by Melty; do not expose an unauthenticated command socket to LAN/WAN clients.

## Message envelope

    {
      "protocol": 1,
      "sessionId": "opaque-session-id",
      "eventId": "unique-event-id",
      "sourceGame": "minecraft-java",
      "sourcePlayer": "opaque-player-id",
      "tick": 12345,
      "type": "mob.spawned",
      "payload": {}
    }

## Release-one message types

- player.join, player.leave, player.position, session.roster
- mob.spawned, mob.damage
- gta.police.spawn_request, gta.police.unit_damaged, combat.outcome
- minecraft.explosion, gta.explosion.observed, gta.explosion.request, minecraft.explosion.request

Validate payload shape, ownership, coordinate bounds, and protocol version at the receiving component. Use event IDs for duplicate suppression and ticks for ordering. Combat authority, damage values, blast radius, and spawn counts remain unset until calibrated in live gameplay.

## Multiplayer acceptance criteria

Run the packaged release twice using Melty's test procedure: one host and one joiner. Verify Melty's join address is used, inspect both logs, confirm both clients see the same encounter and roster, damage a mob, observe police reacting, and trigger one explosion that yields exactly one corresponding event per game. Do not claim public internet connectivity from a localhost-only test.

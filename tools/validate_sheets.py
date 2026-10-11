#!/usr/bin/env python3
"""Check JSON syntax and internal references only; this does not test game code."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "games.json", "systems.json", "entities.json", "events.json",
    "hooks.json", "multiplayer.json", "credits_license.json", "preflight.json"
]
data = {}
errors: list[str] = []

for name in FILES:
    path = ROOT / "design" / name
    try:
        data[name] = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{name}: invalid JSON: {exc}")

if not errors:
    system_ids = {x.get("id") for x in data["systems.json"].get("systems", [])}
    event_ids = {x.get("id") for x in data["events.json"].get("events", [])}
    game_ids = {x.get("id") for x in data["games.json"].get("games", [])}

    for row in data["events.json"].get("events", []):
        if row.get("system") not in system_ids:
            errors.append(f"events.json: {row.get('id')} references missing system {row.get('system')}")
        for consumer in row.get("consumers", []):
            if consumer not in system_ids and consumer not in game_ids and not consumer.startswith("bridge/"):
                errors.append(f"events.json: {row.get('id')} references unknown consumer {consumer}")

    for row in data["systems.json"].get("systems", []):
        for event_id in row.get("inputs", []) + row.get("outputs", []):
            if event_id not in event_ids:
                errors.append(f"systems.json: {row.get('id')} references missing event {event_id}")

    for filename, key in (("systems.json", "systems"), ("entities.json", "entities"), ("hooks.json", "hooks")):
        for row in data[filename].get(key, []):
            for system in row.get("systems", []):
                if system not in system_ids:
                    errors.append(f"{filename}: {row.get('id')} references missing system {system}")
            for event in row.get("events", []):
                if event not in event_ids:
                    errors.append(f"{filename}: {row.get('id')} references missing event {event}")

if errors:
    print("STRUCTURAL CHECK: FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"STRUCTURAL CHECK: PASS — parsed {len(FILES)} JSON sheets; key references resolve.")
print("RELEASE PREFLIGHT: BLOCKED — structural checks are not a game build or gameplay test.")

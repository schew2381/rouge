#!/usr/bin/env python3
import tcod

from Files.input_handlers import EventHandler
from Files.entity import Entity
from Files.engine import Engine
from Files.procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}
    game_map = generate_dungeon(map_width, map_height)
    engine = Engine(entities, event_handler, game_map, player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Rouge",
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(root_console, context)
            engine.handle_events(tcod.event.wait())


if __name__ == "__main__":
    main()

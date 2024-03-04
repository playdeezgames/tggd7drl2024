import grimoire
import item_types
OFFSET_X = grimoire.BOARD_COLUMNS
OFFSET_Y = 0


def draw(my_context):
    world = my_context.get_world()

    y = OFFSET_Y

    my_context.write_text_xy((OFFSET_X, y), f"Sc:{world.score}", 2)
    y += 1

    my_context.write_text_xy((OFFSET_X, y), f"HP:{world.health}/{world.maximum_health}", 4)
    y += 1

    my_context.write_text_xy((OFFSET_X, y), f"EN:{world.energy}/{world.maximum_energy}", 3)
    y += 1

    copper_count = world.get_item_count(item_types.COPPER)
    item_type = item_types.TABLE[item_types.COPPER]
    my_context.write_text_xy((OFFSET_X, y), f"{copper_count}{item_type.text}", item_type.color)
    y += 1

    pass

import grimoire
import item_types
import statistics

OFFSET_X = grimoire.BOARD_COLUMNS
OFFSET_Y = 0


def draw(my_context):
    world = my_context.get_world()

    y = OFFSET_Y

    my_context.write_text_xy((OFFSET_X, y), f"Sc:{world.get_score()[0]}", 2)
    y += 1

    stat = world.get_health()
    my_context.write_text_xy((OFFSET_X, y), f"HP:{stat[0]}/{stat[2]}", 12)
    y += 1

    stat = world.get_energy()
    my_context.write_text_xy((OFFSET_X, y), f"EN:{stat[0]}/{stat[2]}", 3)
    y += 1

    stat = world.get_experience()
    my_context.write_text_xy((OFFSET_X, y), f"XP:{stat[0]}/{stat[2]}", 5)
    y += 1

    stat = world.get_experience_level()
    my_context.write_text_xy((OFFSET_X, y), f"LV:{stat[0]}", 5)
    y += 1

    copper_count = world.get_item_count(item_types.COPPER)
    item_type = item_types.TABLE[item_types.COPPER]
    my_context.write_text_xy((OFFSET_X, y), f"{copper_count}{item_type.text}", item_type.color)
    y += 1

    pass

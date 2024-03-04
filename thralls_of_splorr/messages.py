import grimoire

ROWS = grimoire.CELL_ROWS - grimoire.BOARD_ROWS
COLUMNS = grimoire.CELL_COLUMNS
OFFSET_X = 0
OFFSET_Y = grimoire.BOARD_ROWS
CELL_COUNT = COLUMNS * ROWS

grid = [[(7, " ") for _ in range(0, COLUMNS)] for _ in range(0, ROWS)]
cell_index = 0


def write(text, color):
    global cell_index
    for character in text:
        if cell_index % COLUMNS == 0:
            grid.pop(0)
            grid.append([(7, " ") for _ in range(0, COLUMNS)])
            cell_index = 0
        grid[ROWS - 1][cell_index] = (color, character)
        cell_index += 1


def write_line(text, color):
    global cell_index
    write(text, color)
    cell_index = COLUMNS


def draw(my_context):
    for y in range(ROWS):
        for x in range(COLUMNS):
            cell = grid[y][x]
            my_context.write_text_xy((x, y + OFFSET_Y), cell[1], cell[0])

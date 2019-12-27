from enum import Enum


class MazeCellType(Enum):
    EMPTY = 1
    BLOCK = 2
    START_DOOR = 3
    TARGET_DOOR = 4
    DOOR = 5


class Maze:
    def __init__(self, height, width, cell_size):
        num_rows = height // cell_size
        num_cols =  width // cell_size

        self.maze_cells = []

        for i in range(num_rows):
            if i == 0 or i == num_rows - 1:
                row = [MazeCellType.BLOCK] * num_cols
            else:
                row = [MazeCellType.EMPTY] * num_cols
                row[0], row[-1] = MazeCellType.BLOCK, MazeCellType.BLOCK

            self.maze_cells.append(row)

        self.cell_size = cell_size

    def set_pixel(self, pixel_x, pixel_y, cell_type):
        row = pixel_y//self.cell_size
        col = pixel_x//self.cell_size
        self.maze_cells[row][col] = cell_type

    def set_position(self, row, col, cell_type):
        self.maze_cells[row][col] = cell_type

    def save_maze(self, maze_path="level.lvl"):
        with open(maze_path, 'w') as fw:
            fw.write(str(self.cell_size) + "\n")

            for maze_row in self.maze_cells:
                for cell in maze_row:
                    fw.write(str(cell.value) + ",")
                fw.write("\n")

    def load_maze(self, maze_path="level.lvl"):
        if maze_path == "":
            return
        with open(maze_path) as fr:
            self.cell_size = int(fr.readline())

            lines = fr.readlines()

        self.maze_cells = []

        for line in lines:
            cells_str = line.split(',')
            row_cells = []

            for cell in cells_str:
                if cell == '\n':
                    break
                row_cells.append(MazeCellType(int(cell)))

            self.maze_cells.append(row_cells)
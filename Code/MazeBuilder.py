import pygame

from Graph import Graph
from Maze import Maze
from Maze import MazeCellType
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from Utils import ShortestPathBFS


class MazeBuilder:
    def __init__(self, maze, algorithm_type, w=800, h=600):
        self.maze = maze
        self.screen = pygame.display.set_mode((w, h))
        self.algorithm_type = algorithm_type

    def draw_maze(self):
        cell_size = self.maze.cell_size

        for i_row, maze_row in enumerate(self.maze.maze_cells):
            for i_col, cell in enumerate(maze_row):
                if cell == MazeCellType.BLOCK:
                    color = (0, 0, 0)
                elif cell == MazeCellType.START_DOOR:
                    color = (0, 255, 0)
                elif cell == MazeCellType.TARGET_DOOR:
                    color = (255, 0, 0)
                elif cell == MazeCellType.DOOR:
                    color = (255, 255, 0)
                elif cell == MazeCellType.EMPTY:
                    color = (255, 255, 255)

                rect = pygame.Rect(i_col*cell_size, i_row*cell_size, cell_size, cell_size)
                pygame.draw.rect(self.screen, color, rect)

                if [i_row, i_col] in self.maze_shortest_path[0:self.animation_index_maze]:
                    color = (0, 0, 255)
                    half_cell_size = int(cell_size/2.0)
                    pos = (i_col * cell_size + half_cell_size, i_row * cell_size + half_cell_size)
                    pygame.draw.circle(self.screen, color, pos,half_cell_size)

    def build(self):
        pygame.init()
        clock = pygame.time.Clock()

        running = True
        mode = MazeCellType.BLOCK

        root = tk.Tk()

        self.maze_shortest_path = []
        self.animation_index_maze = 0

        while running:
            pygame_event_list = pygame.event.get()

            for event in pygame_event_list:
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            if self.maze_shortest_path != []:
                if self.animation_index_maze == len(self.maze_shortest_path):
                    continue

                self.animation_index_maze += 1
            else:
                for event in pygame_event_list:
                    if event.type == pygame.KEYDOWN:
                        # root = tk.Tk()
                        if event.key == pygame.K_b:
                            mode = MazeCellType.BLOCK
                        elif event.key == pygame.K_e:
                            mode = MazeCellType.EMPTY
                        elif event.key == pygame.K_s:
                            mode = MazeCellType.START_DOOR
                        elif event.key == pygame.K_t:
                            mode = MazeCellType.TARGET_DOOR
                        elif event.key == pygame.K_d:
                            mode = MazeCellType.DOOR
                        elif event.key == pygame.K_k:
                            path = tk.filedialog.asksaveasfilename(initialdir = "./levels",title = "Save Maze file")
                            if path != "":
                                self.maze.save_maze(path)
                            root.withdraw()
                        elif event.key == pygame.K_l:
                            path = tk.filedialog.askopenfilename(initialdir="./levels", title="Select Maze file")
                            if path != "":
                                self.maze.load_maze(path)
                            root.withdraw()
                        elif event.key == pygame.K_RETURN:
                            self.simulation_started = True
                            self.graph = Graph(self.maze, self.algorithm_type)
                            graph_shortest_path = self.graph.find_shortest_path()

                            ## Student Code:
                            # Given the graph shortest Path, which is a list of coordinates of the nodes,
                            # then get the path from each node to its successor
                            # Hint: Use the ShortesTPathBFS class.
                            # Store the full shortest path on the maze (list of every cell coordinates)
                            # in self.maze_shortest_path variable so that the animation can be done.
                            #
                            #
                            #
                            ##############################################################################
                            #for i in range(0 , len(graph_shortest_path) - 1):
                            tmp = ShortestPathBFS.get_shortest_path(self.maze.maze_cells, graph_shortest_path[0], graph_shortest_path[len(graph_shortest_path)-1])
                            print('#############')
                            print(tmp)
                            print('#############')
                            for i in range(0 , len(tmp)):
                                self.maze_shortest_path.append(tmp[i])
                            print(self.maze_shortest_path)
                            self.maze_shortest_path.append(graph_shortest_path[len(graph_shortest_path)-1])



                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    self.maze.set_pixel(x, y, mode)

            clock.tick(60)
            self.draw_maze()
            pygame.display.flip()

        self.maze.save_maze()

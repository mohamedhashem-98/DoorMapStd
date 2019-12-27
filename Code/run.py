from Graph import GraphAlgorithm
from Maze import Maze
from MazeBuilder import MazeBuilder

if __name__ == '__main__':
    width = 800
    height = 600
    cell_size = 25

    #maze = Maze(height, width, cell_size)
    #mazeBuilder = MazeBuilder(maze, GraphAlgorithm.DIJKSTRA, width, height)
    #mazeBuilder.build()

    maze = Maze(height, width, cell_size)
    mazeBuilder = MazeBuilder(maze, GraphAlgorithm.ASTAR, width, height)
    mazeBuilder.build()
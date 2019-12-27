# todo: get a map as input, transform the map to a graph based on BFS algorithm.
#       For each edge calculate the cost and for each node, calculate the Heuristic
from Maze import MazeCellType
from Utils import ShortestPathBFS
import math


class Maze2Graph:
    def __init__(self, maze_2d, cell_size):
        self.maze = maze_2d
        self.cell_size = cell_size

    def transform2Graph(self):
        graph_nodes = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.DOOR]
        start = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.START_DOOR][0]
        target = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.TARGET_DOOR][0]

        graph_nodes.insert(0, start)
        graph_nodes.append(target)

        graph_edges = []
        x = []
        for i in range(len(graph_nodes)):
            graph_edges.append([])

        ## Student Code: Connect Edges,
        # for each node,
        #   Find the reachable doors. Hint: use BFS on the given array
        #   Add an edge between the current node and each reachable doors
        my_list = []
        for i in range(len(graph_nodes)):
            my_list.append(graph_nodes[i][0])
        def check_steps(steps):
            for i in range(1,len(steps)):
                if steps[i] in my_list:
                    return False
            return True

        tmp = []
        for i in range(len(graph_nodes)):
            tmp=[]
            for j in range(len(graph_nodes)):
                if graph_nodes[i] == graph_nodes[j]:
                    continue
                steps = ShortestPathBFS.get_shortest_path(self.maze, graph_nodes[i][0], graph_nodes[j][0])
                if (check_steps(steps)):
                    tmp.append((j, len(steps)))

            graph_edges[i] = tmp


#[[(2, 2)], [(2, 4), (3, 4)], [(0, 2), (1, 4)], [(1, 4)]]
        print("Graph Edges Are: \n")
        print(graph_edges)
        print('Target is {}'.format(target))
        print('START'+str(start))
        ## Student Code: Calculate H(n)
        #   After adding the edges, loop on the node and calculate the H(n) where n is the node index
        #   H(n) is saved as the second value in the node,
        #   where the first value is its original location in the maze
        #   Hint: H(n) is the euclidian distance between the node and the Target Node
        #
        #
        ###############################################################
        #print(graph_nodes)
        #print('Y is '+str(graph_nodes[0][0][1])) #Y
        #print('X is '+str(graph_nodes[0][0][0]))  #X
        #print('Euclidean is '+str(graph_nodes[0][1]))  #Euc

        for i in range(len(graph_nodes)):
            X = graph_nodes[i][0][0] - target[0][0]
            Y = graph_nodes[i][0][1] - target[0][1]
            graph_nodes[i][1] = int(math.sqrt((math.pow(X, 2)) + (math.pow(Y, 2))))

        print(graph_nodes)


        ## Output for Test Case: debugging_level.lvl
        # Comment/remove this line when you are done
        #return graph_nodes, [[(2, 2)], [(2, 4), (3, 4)], [(0, 2), (1, 4)], [(1, 4)]]
        #########################################################################################

        return graph_nodes, graph_edges

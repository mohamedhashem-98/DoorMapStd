from enum import Enum
from Maze2Graph import Maze2Graph


class GraphAlgorithm(Enum):
    ASTAR = 1,
    DIJKSTRA = 2


class Graph:
    def __init__(self, maze, algorithm_type):
        self.graph_nodes, self.graph_edges = Maze2Graph(maze.maze_cells, maze.cell_size).transform2Graph()
        self.graph_algorithm = algorithm_type

    def find_shortest_path(self):
        ## Path for the debugging_level.lvl
        # remove this line when running your code.
        #return [self.graph_nodes[0][0], self.graph_nodes[2][0], self.graph_nodes[1][0], self.graph_nodes[3][0]]
        ########################

        if self.graph_algorithm == GraphAlgorithm.ASTAR:
            return self.__run_astar()

        if self.graph_algorithm == GraphAlgorithm.DIJKSTRA:
            return self.__run_dijkstra()

    def __run_astar(self):
        OpenList = [0 for i in range(0, len(self.graph_nodes)+1)]
        ClosedList = [0 for i in range(0, len(self.graph_nodes)+1)]
        ParentList = [-1 for i in range(0, len(self.graph_nodes)+1)]
        start = 0
        end = len(self.graph_nodes) - 1
        OpenList.append((start, self.graph_nodes[start][1]))
        Graph = [(int)(1e9) for i in range(0, len(self.graph_nodes)+1)]
        GraphH = [(int)(1e9) for i in range(0, len(self.graph_nodes)+1)]
        cur_vertex = (start, self.graph_nodes[start][1])
        Graph[cur_vertex[0]] = 0
        OpenList[cur_vertex[0]] = 1
        while cur_vertex[0] != end:
            for i in range(0, len(self.graph_edges[cur_vertex[0]])):
                if ClosedList[self.graph_edges[cur_vertex[0]][i][0]]:
                    continue
                g = self.graph_edges[cur_vertex[0]][i][1] + Graph[cur_vertex[0]]
                h = self.graph_nodes[self.graph_edges[cur_vertex[0]][i][0]][1]

                if g < Graph[self.graph_edges[cur_vertex[0]][i][0]]:
                    GraphH[self.graph_edges[cur_vertex[0]][i][0]] = g + h
                    Graph[self.graph_edges[cur_vertex[0]][i][0]] = g
                    ParentList[self.graph_edges[cur_vertex[0]][i][0]] = cur_vertex[0]
            ClosedList[cur_vertex[0]] = 1
            indx = None
            maxi = (int)(1e9 + 1000)
            for i in range(0, len(self.graph_nodes)+1):
                if GraphH[i] < maxi and ClosedList[i] == 0:
                    indx = i
                    maxi = Graph[i]
            cur_vertex = (indx, self.graph_nodes[indx][1])
        print('Cost : %d' % (Graph[end]))
        print('Path : ', end='')
        cur = end
        p = []
        while True:
            p.append(cur)
            cur = ParentList[cur]
            if cur == -1:
                break
        p.reverse()
        new_list = []
        for i in range(len(p)):
            new_list.append(self.graph_nodes[p[i]][0])
        print(new_list)
        return new_list

    def __run_dijkstra(self):
        start = 0
        end = len(self.graph_nodes) - 1
        print("Start is {} END is {}".format(start,end))
        Cost = [int(1e9) for i in range(0, len(self.graph_nodes )+1)]
        path = [-1 for i in range(0, len(self.graph_nodes)+1)]
        queue = []
        x = (start, 0)
        queue.append(x)
        while len(queue):
            cur = queue[0]
            del (queue[0])
            tmp = self.graph_edges[cur[0]]
            print(tmp)
            for i in range(0, len(tmp)):
                if tmp[i][1] + cur[1] < Cost[tmp[i][0]]:
                    Cost[tmp[i][0]] = tmp[i][1] + cur[1]
                    queue.append((tmp[i][0], Cost[tmp[i][0]]))
                    path[tmp[i][0]] = cur[0]
        if Cost[end] == ((int)(1e9)):
            return []
        Path = []
        c = end
        while c != start:
            Path.append(c)
            c = path[c]
        Path.append(start)
        Path.reverse()
        print(Path)
        new_list = []
        for i in range(len(Path)):
            new_list.append(self.graph_nodes[Path[i]][0])
        print(new_list)
        return new_list



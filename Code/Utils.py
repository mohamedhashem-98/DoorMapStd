from Maze import MazeCellType


class ShortestPathBFS:
    @staticmethod
    def get_shortest_path(graph, start_node, end_node):
        displacement_row = [-1, -1, -1, 0, 0, 1, 1, 1]
        displacement_col = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited = ShortestPathBFS.init_list(graph, False)
        queue = [start_node]
        visited[start_node[0]][start_node[1]] = True
        path = ShortestPathBFS.init_list(graph)

        while len(queue) > 0:
            parent_current_position = queue[0]
            queue.remove(queue[0])

            if parent_current_position == end_node:
                return ShortestPathBFS.get_path(path, parent_current_position)

            children = []

            for i in range(len(displacement_row)):
                child_row = displacement_row[i] + parent_current_position[0]
                child_col = displacement_col[i] + parent_current_position[1]

                if child_row < 0 or child_col < 0 or child_row >= len(graph) or child_col >= len(graph[0]) \
                        or visited[child_row][child_col] or graph[child_row][child_col] == MazeCellType.BLOCK:
                    continue
                children.append([child_row, child_col])

            for (child_row, child_col) in children:
                visited[child_row][child_col] = True
                queue.append((child_row, child_col))
                path[child_row][child_col] = parent_current_position

        return ShortestPathBFS.get_path(path, end_node)

    @staticmethod
    def init_list(list1, init_val=None):
        ret_list = []
        for i in range(len(list1)):
            list_row = []
            for j in range(len(list1[0])):
                list_row.append(init_val)
            ret_list.append(list_row)
        return ret_list

    @staticmethod
    def get_path(path, pos):
        movement_list = []
        while pos is not None:
            new_pos = path[pos[0]][pos[1]]
            if new_pos is None:
                break
            movement_list.append(list(new_pos))
            pos = new_pos
        return movement_list[::-1]








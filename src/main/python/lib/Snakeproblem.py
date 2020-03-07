class SnakeProblem:

    def __init__(self, snake_length):
        self.snake_length = snake_length

    def __create_grid(self, row, col):
        """
        The function creates a row X col two dimensional list with values starting from 0 to maximum.
        :param row: Number of rows in the grid.
        :param col: Number of columns in the grid.
        :return: Two dimensional list.
        """
        grid = []
        grid_number = 0
        for index_i in range(0, row):
            new_list = []
            for index_j in range(0, col):
                new_list.append(grid_number)
                grid_number += 1
            grid.append(new_list)
        return grid

    def __find_path(self, graph, start, paths, path=[]):
        """
        This function looks for all possible paths for specific length from a source node.
        :param graph: Graph of the given two dimensional list.
        :param start: starting node for a path.
        :return: All possible paths from start node.
        """
        path = path + [start]
        if len(path) == self.snake_length:
            paths.append(path)
        else:
            for node in graph[start]:
                if node in path:
                    pass
                else:
                    self.__find_path(graph, node, paths, path)

    def __create_graph(self, grid):
        """
        creates a graph from the given two dimensional list.
        :param grid: Two dimensional list is given as input.
        :return: A graph
        """

        def add(adj_list, index_i, index_j):
            adj_list.setdefault(index_i, []).append(index_j)
            adj_list.setdefault(index_j, []).append(index_i)

        graph = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j < len(grid[i]) - 1:
                    add(graph, grid[i][j], grid[i][j + 1])
                if i < len(grid) - 1:
                    add(graph, grid[i][j], grid[i + 1][j])
        return graph

    def possible_paths(self, row, col):
        """
        :param row: Number of rows in the grid.
        :param col: Number of columns in the grid.
        :return: Total number of possible paths of specific length in the grid.
        """
        try:
            self.snake_length = int(self.snake_length)
            if self.snake_length < 0:
                return "Length of snake can't be a negative integer."
        except ValueError:
            return "Snake length can't be a character or floating point number."
        try:
            row, col = int(row), int(col)
        except ValueError:
            return "Grid value can't be a character or floating point number."
        if (row < 0) | (col < 0):
            return "Grid values can't be negative integer."
        if row == 1 and col == 1 and self.snake_length == 1:
            return 1
        grid = self.__create_grid(row, col)
        graph = self.__create_graph(grid)
        paths = []
        for a in graph:
            self.__find_path(graph, a, paths)
        return len(paths)

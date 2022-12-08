class Cell():
    def __init__(self, *, position: tuple[int, int], parent=None):
        self.row, self.column = position
        self.parent = parent
        self.successors = []
        self.f = 0 # f(n)
        self.g = 0 # g(n)
        self.h = 0 # h(n)

    def __repr__(self) -> str:
        return f'(row={self.row}, column={self.column})'    

    def manhattan_distance(self, goal):
        h = abs(self.row - goal.row) + abs(self.column - goal.column)
        return h

    def get_path(self):
        path = []
        path.append(self)
        father = self.parent
        while father is not None:
            path.append(father)
            father = father.parent

        return path[::-1]

from collections import namedtuple
Node = namedtuple('Node', ['r','c'])

class Grid:
    def __init__(self, grid, allow_diagonal=False):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0]) if self.R>0 else 0
        self.allow_diagonal = allow_diagonal

    @staticmethod
    def from_text(text):
        lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
        g = []
        for line in lines:
            row = []
            for ch in line.split():
                if ch == '#': row.append(-1)
                else: row.append(int(ch))
            g.append(row)
        return Grid(g)

    def in_bounds(self, n):
        return 0 <= n.r < self.R and 0 <= n.c < self.C

    def passable(self, n):
        return self.grid[n.r][n.c] != -1

    def cost(self, a, b=None):
        return max(1, self.grid[a.r][a.c])

    def neighbors(self, n):
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        if self.allow_diagonal:
            steps += [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr,dc in steps:
            from collections import namedtuple
            Node = namedtuple('Node',['r','c'])
            nb = Node(n.r+dr, n.c+dc)
            if self.in_bounds(nb) and self.passable(nb):
                yield nb

    def show_path(self, path):
        grid_copy = [row[:] for row in self.grid]
        for p in path:
            if grid_copy[p.r][p.c] != -1:
                grid_copy[p.r][p.c] = 'P'
        s = ''
        for row in grid_copy:
            row_s = ' '.join(str(x) for x in row)
            s += row_s + '\n'
        return s

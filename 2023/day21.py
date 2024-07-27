import numpy as np
Point = complex

class Grid:
    def __init__(self, input):
        self.size = len(input.splitlines())
        self.grid = set()
        self.positions = set()
        for y, line in enumerate(input.splitlines()):
            for x, value in enumerate(line):
                if value == "#":
                    self.grid.add(Point(x, y))
                if value == "S":
                    self.positions.add(Point(x, y))
                    
    def step(self):
        newPostion = set()
        for position in self.positions:
            for direction in (1, -1, 1j, -1j):
                if self.wrap(position + direction) not in self.grid:
                    newPostion.add(position + direction)
        self.positions = newPostion

    def wrap(self, point):
        return Point(point.real % self.size, point.imag % self.size)

def part1(input):
    grid = Grid(input)
    for _ in range(64):
        grid.step()
    return len(grid.positions)

def part2(input):
    grid = Grid(input)
    target = (26501365 - 65) // 131
    X, Y = [0, 1, 2], []
    for s in range(65 + 131 * 2 + 1):
        if s % 131 == 65:
            Y.append(len(grid.positions))
        grid.step()
    poly = np.rint(np.polynomial.polynomial.polyfit(X, Y, 2)).astype(int).tolist()
    return sum(poly[i] * target ** i for i in range(3))

print("Part 1: " + str(part1(open("inputs\\day21.txt", "r").read())))
print("Part 2: " + str(part2(open("inputs\\day21.txt", "r").read())))
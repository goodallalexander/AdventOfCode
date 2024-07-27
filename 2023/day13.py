POINT = complex

def isHorizontalFlip(grid, maxX, x, part2):
    flag = False
    for point in grid:
        newPoint = POINT(x + (x + 1 - point.real), point.imag)
        if 0 <= newPoint.real <= maxX and newPoint not in grid:
            if not part2 or flag:
                return False
            flag = True
    return not part2 or flag

def isVerticalFlip(grid, maxY, y, part2):
    flag = False
    for point in grid:
        newPoint = POINT(point.real, y + (y + 1 - point.imag))
        if 0 <= newPoint.imag <= maxY and newPoint not in grid:
            if not part2 or flag:
                return False
            flag = True
    return not part2 or flag

def solve(grid, maxX, maxY, part2 = False):
    for x in range(maxX):
        if isHorizontalFlip(grid, maxX, x, part2):
            return x + 1
    for y in range(maxY):
        if isVerticalFlip(grid, maxY, y, part2):
            return 100 * (y + 1)

def parse(raw):
    maxY = len(raw.splitlines()) - 1
    maxX = len(raw. splitlines()[0]) - 1
    grid = set()
    for y, line in enumerate(raw.splitlines()):
        for x, value in enumerate(line):
            if value == '#':
                grid.add(POINT(x, y))
    return grid, maxX, maxY

def part1(input):
    grids = [parse(raw) for raw in input.read().split('\n\n')]
    return sum(solve(*grid) for grid in grids)

def part2(input):
    grids = [parse(raw) for raw in input.read().split('\n\n')]
    return sum(solve(*grid, True) for grid in grids)


print("Part 1: " + str(part1(open("inputs\day13.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day13.txt", "r"))))
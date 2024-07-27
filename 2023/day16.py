from collections import defaultdict
POINT = complex

def getStraight(direction):
    out = '.'
    if direction.real == 0:
        out += '|'
    elif direction.imag == 0:
        out += '-'
    return out

def getClockwise(direction):
    out = ''
    if direction.real == 0:
        out += '-/'
    if direction.imag == 0:
        out += '|\\'
    return out

def getCounterClockwise(direction):
    out = ''
    if direction.real == 0:
        out += '-\\'
    if direction.imag == 0:
        out += '|/'
    return out

def score(grid, entry, direction):
    seen = defaultdict(list)
    beams = [(entry, direction)]
    while beams:
        newBeams = []
        for position, direction in beams:
            if position not in grid or direction in seen[position]:
                continue
            seen[position].append(direction)

            if grid[position] in getStraight(direction):
                newBeams.append((position + direction, direction))

            if grid[position] in getClockwise(direction):
                newDirection = direction * 1j
                newBeams.append((position + newDirection, newDirection))

            if grid[position] in getCounterClockwise(direction):
                newDirection = direction * -1j
                newBeams.append((position + newDirection, newDirection))
            
        beams = newBeams
    return len(seen)

def part1(input):
    grid = {}
    for y, row in enumerate(input.read().splitlines()):
        for x, value in enumerate(row):
            grid[POINT(x, y)] = value

    return score(grid, 0, 1)

def part2(input):
    grid = {}

    answer = 0
    for y, row in enumerate(input.read().splitlines()):
        for x, value in enumerate(row):
            grid[POINT(x, y)] = value
    for i in range(SHAPE):
        answer = max(answer,
                     score(grid, POINT(i, 0), 1j),
                     score(grid, POINT(i, SHAPE - 1), -1j),
                     score(grid, POINT(0, i), 1),
                     score(grid, POINT(SHAPE - 1, 0), -1)
                     )
    return answer

SHAPE = len(open("inputs\day18.txt", "r").read().splitlines())
print("Part 1: " + str(part1(open("inputs\day16.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day16.txt", "r"))))
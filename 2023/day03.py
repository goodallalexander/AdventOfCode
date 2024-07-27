POINT = complex
adjacentPoints = [POINT(-1, 1),  POINT(0, 1),  POINT(1, 1),
                  POINT(-1, 0),                POINT(1, 0),
                  POINT(-1, -1), POINT(0, -1), POINT(1, -1)]

def part1(input):
    grid, symbols = generateGrid(input)
    parts = set()
    for symbol in symbols:
        parts |= getAdjacentParts(grid, symbol)
    answer = 0
    for part in parts:
        answer += part[1]
    return answer

def part2(input):
    grid, symbols = generateGrid(input)
    answer = 0
    for symbol in symbols:
        if grid[symbol] != "*": continue
        parts = list(getAdjacentParts(grid, symbol))
        if len(parts) == 2:
            answer += parts[0][1] * parts[1][1]
    return answer

def getAdjacentParts(grid, positon): 
    parts = set()
    for direction in adjacentPoints:
        parts.add(getNumber(grid, positon + direction))
    return parts - {None}

def getNumber(grid, positon): 
    if positon not in grid or not grid[positon].isnumeric():
        return None
    
    while positon-1 in grid and grid[positon-1].isnumeric():
        positon -= 1
    start = positon
    number = ""
    while positon in grid and grid[positon].isnumeric():
        number += grid[positon]
        positon += 1
    return start, int(number)

def generateGrid(input): 
    grid = {}
    symbols = []
    for y, line in enumerate(input.read().splitlines()):
        for x, value in enumerate(line):
            if value != ".":
                grid[POINT(x, y)] = value
                if not value.isnumeric():
                    symbols.append(POINT(x, y))
    return grid, symbols

print("Part 1: " + str(part1(open("inputs\day03.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day03.txt", "r"))))
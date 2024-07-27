POINT = complex

def getPath(grid, start, direction):
    path = {}
    position = start
    originalDirection = direction
    while position in grid:
        path[position] = grid[position]
        position += direction
        if position not in grid:
            return None
        if position == start:
            if direction == 1j or originalDirection == -1j:
                path[start] == '|'
            return path
        direction = changeDirection(direction, grid[position])
        if direction == None: #invalid turn
            return None

def changeDirection(direction, pipe):
    if((pipe == '7' and direction == 1) or
       (pipe == 'J' and direction == 1j) or
       (pipe == 'L' and direction == -1) or
       (pipe == 'F' and direction == -1j) ):
        return direction * 1j #rotate 90 degrees to the right
    
    if((pipe == '7' and direction == -1j) or
       (pipe == 'J' and direction == 1) or
       (pipe == 'L' and direction == 1j) or
       (pipe == 'F' and direction == -1) ):
        return direction * -1j #rotate 90 degrees to the left
    
    if pipe in '|-': return direction

def cleanTrash(grid, start):
    return getPath(grid, start, 1) or getPath(grid, start, -1) or getPath(grid, start, 1j)

def part1(input):
    grid = {}
    start = None
    for y,line in enumerate(input.read().splitlines()):
        for x,value in enumerate(line):
            if value != '.':
                grid[POINT(x,y)] = value
                if value == 'S':
                    start = POINT(x,y)
    
    grid = cleanTrash(grid, start)
    return len(grid) // 2

def part2(input):
    grid = {}
    start = None
    for y,line in enumerate(input.read().splitlines()):
        for x,value in enumerate(line):
            if value != '.':
                grid[POINT(x,y)] = value
                if value == 'S':
                    start = POINT(x,y)
    grid = cleanTrash(grid, start)
    answer = 0
    for y in range(len(open("inputs\day10.txt", "r").read().splitlines())):
        inside = False
        for x in range(len(open("inputs\day10.txt", "r").read().splitlines()[0])):
            if POINT(x,y) in grid:
                if grid[POINT(x,y)] in "|JL":
                    inside = not inside
            else:
                answer += inside
    return answer

print("Part 1: " + str(part1(open("inputs\day10.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day10.txt", "r"))))
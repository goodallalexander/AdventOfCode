def spin(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                newY = y
                grid[newY][x] = '.'
                while newY >= 0 and grid[newY][x] == '.':
                    newY -= 1
                grid[newY + 1][x] = 'O'
    return list(map(list, zip(*grid[::-1])))

def cycle(grid):
    for i in range(4):
        grid = spin(grid)
    return grid

def score(grid):
    answer = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                answer += len(grid) - y
    return answer

def part1(input):
    grid = [list(line) for line in input.read().splitlines()]
    spin(grid)
    return score(grid)

def part2(input):
    grid = [list(line) for line in input.read().splitlines()]
    seen = {}
    fastForward = False
    t = 0 
    target = 1000000000
    while t < target:
        grid = cycle(grid)
        t += 1
        h = str(grid)
        if not fastForward and h in seen:
            period = t - seen[h]
            t += ((target - t)//period)*period
            fastForward == True
        seen[h] = t
    return score(grid)

print("Part 1: " + str(part1(open("inputs\day14.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day14.txt", "r"))))
POINT = complex

def solve(raw, empty, part1 = True):
    factor = 1 if part1 else 1000000 - 1
    grid = []
    for point in raw:
        mod = POINT(
            sum(a < point.real for a in empty[0]),
            sum(a < point.imag for a in empty[1])
        ) * factor
        grid.append(point + mod)
    answer = 0
    for i in range(len(grid) - 1):
        for j in range(i + 1, len(grid)):
            answer += int(abs(grid[i].imag - grid[j].imag) + abs(grid[i].real - grid[j].real))
    return answer

def part1(input):
    raw = []
    empty = [set(range(LIM)), set(range(LIM))]

    for y, l in enumerate(input.read().splitlines()):
        for x, value in enumerate(l):
            if value == '#':
                raw.append(POINT(x,y))
                empty[0] -= {x}
                empty[1] -= {y}
    return solve(raw, empty, True)

def part2(input):
    raw = []
    empty = [set(range(LIM)), set(range(LIM))]

    for y, l in enumerate(input.read().splitlines()):
        for x, value in enumerate(l):
            if value == '#':
                raw.append(POINT(x,y))
                empty[0] -= {x}
                empty[1] -= {y}
    return solve(raw, empty, False)


LIM = len(open("inputs\day10.txt", "r").read().splitlines())

print("Part 1: " + str(part1(open("inputs\day11.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day11.txt", "r"))))
import re
from collections import defaultdict

Point = complex

def getDependencies(children, node):
    inDegree = defaultdict(int)
    for parent, kids in children.items():
        for child in kids:
            inDegree[child] += 1

    dependent = -1
    queue = [node]

    while queue:
        i = queue.pop()
        dependent += 1
        for child in children[i]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                queue.append(child)

    return dependent


def part1(input):
    bricks = [list(map(int, re.findall("-?\\d+", line))) + [i] for i, line in enumerate(input.splitlines())]
    bricks.sort(key = lambda b:b[2])
    highestZ = defaultdict(lambda:(0, -1))

    sitsOn = defaultdict(set)
    children = defaultdict(set)

    for brick in bricks:
        x1, y1, z1, x2, y2, z2, index = brick
        newZ = 0

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                newZ = max(newZ, highestZ[Point(x, y)][0])
        
        height = z2 - z1 + 1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                old = highestZ[Point(x, y)]
                if old[0] == newZ:
                    sitsOn[index].add(old[1])
                    children[old[1]].add(index)
                highestZ[Point(x, y)] = (newZ + height, index)

    for child in children[-1]:
        del sitsOn[child]
    del children[-1]

    unsafe = set()

    for k, v in sitsOn.items():
        if len(v) == 1:
            unsafe |= v

    return len(bricks) - len(unsafe)

def part2(input):
    bricks = [list(map(int, re.findall("-?\\d+", line))) + [i] for i, line in enumerate(input.splitlines())]
    bricks.sort(key = lambda b:b[2])
    highestZ = defaultdict(lambda:(0, -1))

    sitsOn = defaultdict(set)
    children = defaultdict(set)

    for brick in bricks:
        x1, y1, z1, x2, y2, z2, index = brick
        newZ = 0

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                newZ = max(newZ, highestZ[Point(x, y)][0])
        
        height = z2 - z1 + 1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                old = highestZ[Point(x, y)]
                if old[0] == newZ:
                    sitsOn[index].add(old[1])
                    children[old[1]].add(index)
                highestZ[Point(x, y)] = (newZ + height, index)

    for child in children[-1]:
        del sitsOn[child]
    del children[-1]

    unsafe = set()

    for k, v in sitsOn.items():
        if len(v) == 1:
            unsafe |= v

    answer = 0
    for brick in unsafe:
        answer += getDependencies(children, brick)

    return answer

print("Part 1: " + str(part1(open("inputs\\day22.txt", "r").read())))
print("Part 2: " + str(part2(open("inputs\\day22.txt", "r").read())))
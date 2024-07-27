import re
from math import lcm

def loop(instruction):
    instruction = [0 if ins == 'L' else 1 for ins in instruction]
    while True:
        yield from instruction

def solve(instruction, network, position):
    answer = 0
    if position not in network:
        return "ERROR"
    for i in loop(instruction):
        if position[-1] == 'Z': break
        answer += 1
        position = network[position][i]
    return answer

def part1(input):
    instructions, nodes = input.read().split("\n\n")
    network = {}

    for line in nodes.splitlines():
        source, left, right = re.findall(r"[A-Z]+", line)
        network[source] = (left, right)

    position = 'AAA'
    return solve(instructions, network, position)

def part2(input):
    instructions, nodes = input.read().split("\n\n")
    network = {}

    for line in nodes.splitlines():
        source, left, right = re.findall(r"[A-Z]+", line)
        network[source] = (left, right)

    periods = []
    for n in filter(lambda x: x[-1] == 'A', network):
        periods.append(solve(instructions, network, n))
    return lcm(*periods)


print("Part 1: " + str(part1(open("inputs\day08.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day08.txt", "r"))))
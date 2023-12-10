#Day 8: Haunted Wasteland
#You're travling through a desert using a (convoluted) map as a guide.
#Input is a "map" at the top is a sequence of "L"s and "R"s and then nodes represented like so GQK = (FVS, VDC).
#Part 1: Starting at "AAA" how many steps are required to reach "ZZZ", given you navigate the map by going to the left or right node listed on the current node by following the sequence at the top of the input?
#Part 2: As above but starting at all nodes ending in "A", how many steps until all are at a node ending in "Z"?

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
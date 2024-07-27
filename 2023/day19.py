import re
from copy import deepcopy

class PartRange:
    def __init__(self, ranges = None):
        self.ranges = deepcopy(ranges) or {l:[0, 4001] for l in "xmas"}

    def splitOn(self, leftHandSide):
        inRange = PartRange(self.ranges)
        outRange = PartRange(self.ranges)
        number = int(leftHandSide[2:])
        existingRange = inRange.ranges[leftHandSide[0]]

        if existingRange[0] <= number <= existingRange[1]:
            if leftHandSide[1] == '>':
                inRange.ranges[leftHandSide[0]][0] = number
                outRange.ranges[leftHandSide[0]][1] = number + 1

            else: # <
                inRange.ranges[leftHandSide[0]][1] = number
                outRange.ranges[leftHandSide[0]][0] = number - 1

        elif number < existingRange[0] and leftHandSide[1] == '>':
            outRange = None

        elif number > existingRange[1] and leftHandSide[1] == '<':
            outRange = None

        else:
            inRange = outRange = None
        return inRange, outRange
    
    def inRange(self, *args):
        for l, v in zip("xmas", args):
            if not self.ranges[l][0] < v < self.ranges[l][1]:
                return False
        return True
    
    def score(self):
        answer = 1
        for l, h in self.ranges.values():
            answer *= h - l - 1
        return answer
            
def part1(input):
    workflow_raw, parts = input.read().split("\n\n")

    workflows = {}

    for line in workflow_raw. splitlines():
        name, rules = line[:-1].split("{")
        workflows[name] = rules.split(",")

    validRanges = []

    def testRange(partRange, name):
        if partRange is None: return
        if name in "AR":
            if name == "A":
                validRanges.append(partRange)
        else:
            rules = workflows[name]
            for rule in rules:
                if ":" not in rule:
                    testRange(partRange, rule)
                else:
                    leftHandSide, next = rule.split(":")
                    inRange, outRange = partRange.splitOn(leftHandSide)
                    testRange(inRange, next)
                    partRange = outRange
                    if partRange == None: return

    testRange(PartRange(), "in")

    answer = 0

    for part in parts.splitlines():
        x, m ,a ,s = map(int, re.findall(r"\d+", part))
        if any(pr.inRange(x, m, a, s) for pr in validRanges):
            answer += x + m + a + s

    return answer

def part2(input):
    workflow_raw, parts = input.read().split("\n\n")

    workflows = {}

    for line in workflow_raw. splitlines():
        name, rules = line[:-1].split("{")
        workflows[name] = rules.split(",")

    validRanges = []

    def testRange(partRange, name):
        if partRange is None: return
        if name in "AR":
            if name == "A":
                validRanges.append(partRange)
        else:
            rules = workflows[name]
            for rule in rules:
                if ":" not in rule:
                    testRange(partRange, rule)
                else:
                    leftHandSide, next = rule.split(":")
                    inRange, outRange = partRange.splitOn(leftHandSide)
                    testRange(inRange, next)
                    partRange = outRange
                    if partRange == None: return

    testRange(PartRange(), "in")

    return sum(pr.score() for pr in validRanges)

print("Part 1: " + str(part1(open("inputs\day19.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day19.txt", "r"))))
class Solver:
    def __init__(self):
        self.perimeter = 0
        self.points = [(0, 0)]
        self.position = [0, 0]

    def addInstruction(self, direction, length):
        directions = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1),
                      "0": (1, 0), "1": (0, 1), "2": (-1, 0), "3": (0, -1)}
        self.perimeter += length
        direction = directions[direction]
        self.position[0] += length * direction[0]
        self.position[1] += length * direction[1]
        self.points.append(tuple(self.position))

    def solve(self):
        area = 0
        for (x1, y1), (x2, y2) in zip(self.points[:-1], self.points[1:]):
            area += (x2 - x1) * (y2 + y1)
        return abs(int(area)) // 2 + self.perimeter // 2 + 1
    

def part1(input):
    answer = Solver()
    for direction, length, colour in [line.split() for line in input.read().splitlines()]:
        answer.addInstruction(direction, int(length))
    return answer.solve()

def part2(input):
    answer = Solver()
    for direction, length, colour in [line.split() for line in input.read().splitlines()]:
        length = colour[2:-2]
        direction = colour[-2]
        answer.addInstruction(direction, int(length, base = 16))
    return answer.solve()

print("Part 1: " + str(part1(open("inputs\day18.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day18.txt", "r"))))
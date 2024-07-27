import re
from sympy import Symbol, solve_poly_system

class Hailstone:
    def __init__(self, line):
        x, y, z, velocityX, velocityY, velocityZ = map(int, re.findall(r"-?\d+", line))
        self.positon = [x, y, z]
        self.velocity = [velocityX, velocityY, velocityZ]

    def line_intersection(self, other):
        x, y, _ = self.positon
        velocityX, velocityY, _ = self.velocity
        line1 = ((x, y), (x + velocityX, y + velocityY))
        x, y, _ = other.positon
        velocityX, velocityY, _ = other.velocity
        line2 = ((x, y), (x + velocityX, y + velocityY))
        xDifference = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        yDifference = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def detect(xDifference, yDifference):
            return xDifference[0] * yDifference[1] - xDifference[1] * yDifference[0]
        
        div = detect(xDifference, yDifference)
        if div == 0:
            return None, None
        
        d = (detect(*line1), detect(*line2))
        x = detect(d, xDifference) / div
        y = detect(d, yDifference) / div

        if self.is_in_future(x) and other.is_in_future(x):
            return x, y

        return None, None
    
    def is_in_future(self, newX):
        x = self.positon[0]
        velocityX = self.velocity[0]
        return (newX - x) / velocityX >= 0


def part1(input):
    hailstones = [Hailstone(line) for line in input.splitlines()]
    testArea = (200000000000000, 400000000000000)
    answer = 0
    for i in range(len(hailstones) - 1):
        for j in range(i + 1, len(hailstones)):
            x, y = hailstones[i].line_intersection(hailstones[j])
            if x is None: continue
            if testArea[0] <= x <= testArea[1] and testArea[0] <= y <= testArea[1]:
                answer += 1
    return answer

def part2(input):
    hailstones = [Hailstone(line) for line in input.splitlines()]
    x,y,z,vx,vy,vz = (Symbol(c) for c in "x,y,z,vx,vy,vz".split(","))
    positon = [x, y, z]
    velocity = [vx, vy, vz]
    vars = [*positon, *velocity]
    eqs = []
    for i, hs in enumerate(hailstones[:3]):
        t = Symbol(f"t_{i}")
        for j in range(3):
            eqs.append(positon[j]+velocity[j]*t - (hs.positon[j] + hs.velocity[j]*t))
        vars.append(t)
    return sum(solve_poly_system(eqs, vars)[0][:3])

print("Part 1: " + str(part1(open("inputs\\day24.txt", "r").read())))
print("Part 2: " + str(part2(open("inputs\\day24.txt", "r").read())))
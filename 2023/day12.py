import re

def solve(line, numbers, part2 = False):
    if part2:
        numbers *= 5
        line = "?".join([line]*5)
    DP = {}

    def f(i, n, b): # i - index in line, n - index in numbers, b - size of current block
        if (i, n, b) in DP: return DP[(i, n, b)]
        if i == len(line):
            return int( (n == len(numbers) and b == 0) or (n == len(numbers) - 1 and b == numbers[-1]) )
        
        answer = 0
        if line[i] in ".?":
            if b == 0:
                answer += f(i + 1, n ,0)
            else:
                if n == len(numbers): return 0
                if b == numbers[n]:
                    answer += f(i + 1, n + 1, 0)

        if line[i] in "#?":
            answer += f(i + 1, n, b + 1)

        DP[(i, n, b)] = answer
        return answer
    return f(0, 0, 0)
            

def parseLine(line):
    line = re.sub(r"\.+", ".", line)
    leftSide, rightSide = line.split()
    numbers = eval(rightSide)
    return leftSide, numbers

def part1(input):
    input = [parseLine(line) for line in input.read().splitlines()]

    return sum(solve(line, number) for line, number in input)

def part2(input):
    input = [parseLine(line) for line in input.read().splitlines()]

    return sum(solve(line, number, part2 = True) for line, number in input)


print("Part 1: " + str(part1(open("inputs\day12.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day12.txt", "r"))))
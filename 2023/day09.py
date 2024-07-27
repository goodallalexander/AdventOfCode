def solve(numbers):
    if all(n == 0 for n in numbers):
        return 0
    difference = []
    for i in range(len(numbers) - 1):
        difference.append( numbers[i + 1] - numbers[i])
    return numbers[-1] + solve(difference)

def part1(input):
    inputNumbers = [list( map( int, line.split() ) ) for line in input.read().splitlines()]
    return sum(solve(numbers) for numbers in inputNumbers)

def part2(input):
    inputNumbers = [list( map( int, line.split() ) ) for line in input.read().splitlines()]
    return sum(solve(numbers[::-1]) for numbers in inputNumbers)

print("Part 1: " + str(part1(open("inputs\day09.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day09.txt", "r"))))
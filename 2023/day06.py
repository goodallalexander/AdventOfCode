import math
import re

def findMargin(time, distance):
    distance += 1e-6 
    low = int( (time - math.sqrt(time**2 - 4 * distance))/2 )
    high = int( (time + math.sqrt(time**2 - 4 * distance))/2 )
    return high - low

def part1(input):
    numbers = list( map(int, re.findall(r"\d+", input.read())) )
    numberRaces = len(numbers)//2
    answer = 1
    for i in range(numberRaces):
        answer *= findMargin(numbers[i], numbers[i + numberRaces])
    return answer

def part2(input):
    input = input.read().replace(" ", "")
    numbers = list( map(int, re.findall(r"\d+", input)) )
    numberRaces = len(numbers)//2
    answer = 1
    for i in range(numberRaces):
        answer *= findMargin(numbers[i], numbers[i + numberRaces])
    return answer

print("Part 1: " + str(part1(open("inputs\day06.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day06.txt", "r"))))
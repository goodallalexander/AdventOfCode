#Day 6: Wait For It
#You're competing in a boat race, you propell the boat by pressing down a button for some amount of milliseconds, afterwards the boat's speed will be depenant on how long the button was held down, e.g. x milliseconds = a speed of x.
#The input is a list of race times and the record distance traveled in those times.
#Part 1: Determine the number of ways to beat each race and then multiply these values together.
#Part 2: Turns out the input has some bad kering and there is only one race, how many ways can you beat the record?

import math
import re

def findMargin(time, distance):
    distance += 1e-6 #need to at least beat the distance
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
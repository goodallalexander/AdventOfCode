import re

def part1(input):
    count = 0
    for line in input:
        valid = True
        gameData = line[5:].strip().split(": ") 
        gameID = int(gameData[0])
        sets = re.split("; ", gameData[1]) 
        for item in sets:
            rounds = item.split(", ")
            
            for cubes in rounds:
                subset = cubes.split(" ") 
                if int(subset[0]) > 12 and subset[1] == "red": 
                    valid = False
                    break
                if int(subset[0]) > 13 and subset[1] == "green":
                    valid = False
                    break
                if int(subset[0]) > 14 and subset[1] == "blue":
                    valid = False
                    break

        if valid:
            count += gameID
    return count  

def part2(input):
    sumOfPower = 0
    for line in input:
        colours = {"red": [], "blue": [], "green": []}

        gameData = line[5:].strip().split(": ")
        gameData = re.split(", |; ", gameData[1].strip())

        for item in gameData:
            cubeColourCount = item.split(" ")
            colours[cubeColourCount[1]].append(int(cubeColourCount[0]))
        
        power = 1
        for value in colours:
            power *= max(colours[value])
        sumOfPower += power

    return sumOfPower

print("Part 1: " + str(part1(open("inputs\day02.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day02.txt", "r"))))
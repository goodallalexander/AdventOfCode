#Day 2: Cube Conundrum
#You're playing a (boring) game with an elf to kill time, each game the elf will pull out some cubes from a bag and then returning them, the elf may repeat this multiple times
#The puzzle input is the records of 100 games e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" or "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#Part 1: Determine which games are valid if the bad contains 12 red cubes, 13 green cubes, and 14 blue cubes, and output the sum of the game IDs of these valid games
#Part 2: The power of a game is the fewest number of each colour of cube multiplied together, output the sum of the power of all games

import re

def part1(input):
    count = 0
    for line in input:
        valid = True
        gameData = line[5:].strip().split(": ") #splits the gameID from the rest of the game's data
        gameID = int(gameData[0])
        sets = re.split("; ", gameData[1]) #converts to list of game rounds
        for item in sets:
            rounds = item.split(", ")
            
            for cubes in rounds:
                subset = cubes.split(" ") #converts to list of <number of cubes>, <colour of cube>
                #hard coded game rules
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
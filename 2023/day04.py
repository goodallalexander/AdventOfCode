#Day 4: Scratchcards
#An elf has a lot of scratch cards, help them find out what they've won
#Input is a list of scratch crad games with the gameID, the winning numbers, and then the player's numbers, e.g. Card   1: 34 55 49 53 46  7 82 22 59 33 | 33 29  7 66 22 51 59 21 55 85 53 26 94 46 24 82  6 47 38  2 34 89 49 41 76
#Part 1: What is the elf's score accoss all games if 1 match is 1 point, 2 matches is 2 points, 3 matches is 4 points, 4 matches is 8 points, and so on.
#Part 2: Instead of winning points you instead win coppies of future scratch cards, how many cards does the elf with if the proccess stops when a crad wins no more cards? Card wins like this: if game 1 won 3 matches, you would win 1 coppy of game 2, 3, and 4

def part1(input):
    totalScore = 0
    for game in input:
        numberOfMatches = findMatches(game)
        totalScore += int(2**(numberOfMatches-1))
    return totalScore

def part2(input):
    cards = [1] * NUMBEROFGAMES
    for card, game in enumerate(input.read().splitlines()):
        numberOfMatches = findMatches(game)
        for i in range(numberOfMatches):
            cards[card + i + 1] += cards[card]
    return sum(cards)

def findMatches(game):
    _, game = game.split(":")
    winningNumbers, ownedNumbers = game.split("|")
    return len( set(winningNumbers.split()) & set(ownedNumbers.split()) ) 

NUMBEROFGAMES = len(open("inputs\day04.txt", "r").read().splitlines())

print("Part 1: " + str(part1(open("inputs\day04.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day04.txt", "r"))))
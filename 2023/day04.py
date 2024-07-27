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
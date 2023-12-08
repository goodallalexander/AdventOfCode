#Day 7: Camel Cards
#You are playing a game like poker
#Input is a list of hands and the corisponding bet e.g. 32T3K 765
#Part 1: Order the hands in order of hand type (Five of a kind > Four of a kind > Full house > Three of kind > Two pair > One pair > High card) and then by card value left to right. 
#        Multiply the bid by it's new position in the list and sum them all together.
#Part 2: As part 1 but "J" are now wild card, it is used to make the best possible hands, and its value is lowest  in tie breakers

from collections import Counter

def translate(card, part1 = True):
    if card.isnumeric():
        return int(card)
    return {
        "T": 10,
        "J": 11 if part1 else 1,
        "Q": 12,
        "K": 13,
        "A": 14
    }[card]

class Hand:
    def __init__(self, line, part1 = True):
        raw, bid = line.split()
        self.bid = int(bid)
        self.cards = tuple(translate(card, part1) for card in raw)
        self.type = self.getType(part1)

    def __repr__(self):
        return str(self.cards) + "[" + str(self.bid) + "]"
    
    def __lt__(self, other):
        return self.type < other.type or (self.type == other.type and self.cards < other.cards) 
    
    def getType(self, part1):
        counter = Counter(self.cards)
        highest = max(counter.values())

        if part1 == False:
            wilds = counter[1]
            del counter[1]
            highest = wilds
            if counter:
                highest += max(counter.values())

        if highest == 5:
            return 6 #Five of a kind
        elif highest == 4:
            return 5 #Four of a kind
        elif len(counter) == 2:
            return 4 #Full house
        elif highest == 3:
            return 3 #Three of a kind
        elif len(counter) == 3:
            return 2 #Two pair
        elif highest == 2:
            return 1 #one pair
        else:
            return 0 #High card

def part1(input):
    hands = [Hand(line) for line in input.read().splitlines()]
    hands.sort()
    answer = 0
    for i, hand in enumerate(hands):
        answer += (i + 1) * hand.bid
    return answer

def part2(input):
    hands = [Hand(line, False) for line in input.read().splitlines()]
    hands.sort()
    answer = 0
    for i, hand in enumerate(hands):
        answer += (i + 1) * hand.bid
    return answer

print("Part 1: " + str(part1(open("inputs\day07.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day07.txt", "r"))))
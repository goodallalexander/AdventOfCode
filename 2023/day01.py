def part1(input):
    calabration = 0
    for line in input:
        calabration += decode(line)
    return calabration

def part2(input):
    calabration = 0
    for line in input:
        calabration += decode(wordsToNumbers(line))
    return calabration

def decode(s):
    s = "".join(filter(str.isdigit, s))
    s = s[0] + s[-1] 

    return int(s)

def wordsToNumbers(s):

    for word, number in wordsNumbers.items():
        s = s.replace(word, word + number + word)

    return s

wordsNumbers = {"zero": "0",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"}

print("Part 1: " + str(part1(open("inputs\day01.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day01.txt", "r"))))
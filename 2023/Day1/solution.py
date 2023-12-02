#Day 1: Trebuchet?!
#You need to decode the input to get the correct calibration value for the Trebuchet you're in!
#The puzzle input is a file of strings with mixed words and numbers, e.g. "1abc2", "two1nine", "eightwothree", ect.
#Part 1: The calibration value of each string is the first and last digit, e.g. "1abc2" = 12, "19376" = 16
#        Sum all of the calibration values.
#Part 2: Same as Part 1 but any digits as words count as digits, e.g. "two1nine" should be read as "219", and "eightwothree" as "823", ect.

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
    s = "".join(filter(str.isdigit, s)) #filter returns a filter object, thus needs to be joined
    s = s[0] + s[-1] 

    return int(s)

def wordsToNumbers(s):

    for word, number in wordsNumbers.items():
        s = s.replace(word, word + number + word) #replaces to word number word so overlapping words are counted correctly

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

print("Part 1: " + str(part1(open("Day1\input.txt", "r"))))
print("Part 2: " + str(part2(open("Day1\input.txt", "r"))))

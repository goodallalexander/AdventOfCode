def h(input): #Hash function
    value = 0
    for character in input:
        value += ord(character)
        value *= 17
        value %= 256
    return value

def part1(input):
    answer = 0
    for token in input.read().split(","):
        answer += h(token)
    return answer

def part2(input):
    boxes = [[] for _ in range(256)]
    for token in input.read().split(","):
        if "-" in token:
            label = token[:-1]
            boxes[h(label)] = [lens for lens in boxes[h(label)] if lens[0] != label]
        else:
            label, level = token.split('=')
            target = boxes[h(label)]
            replaced = False
            for lens in target:
                if lens[0] == label:
                    lens[1] = int(level)
                    replaced = True
            if not replaced:
                target.append([label, int(level)])

    answer = 0
    for boxNumber, box in enumerate(boxes):
        for slot, (_, level) in enumerate(box):
            answer += (boxNumber + 1) * (slot + 1) * level
    return answer

print("Part 1: " + str(part1(open("inputs\day15.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day15.txt", "r"))))
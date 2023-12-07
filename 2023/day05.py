#Day 5: If You Give A Seed A Fertilizer
#Help a farmer plan an optimal farm by using the latest Almanac(the puzzle input)
#Input is a list of seed numbers followed by maps, these display the destination range start, the source range start, and the range length (e.g. 50 98 2),
#use these maps to conver from seed to soil to fertilizer to water to light to temperature to humidity to location
#Part 1: What is the lowest location number that corresponds to nay of the initial seed numbers?
#Part 2: As part 1, but the seeds line in the input come in pairs, the first value is the start of the range and the second value is the length of that range

class Range:
    def __init__(self, lower, uppper):
        self.lower = lower
        self.upper = uppper
    def __repr__(self):
        return f"[{self.lower}, {self.upper}]"
    def intersection(self, other):
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None
    def subtract(self, other):
        ins = self.intersection(other)
        if ins == None:
            #----       intersect
            #       --  self
            return [Range(self.lower, self.upper)]
        elif(ins.lower, ins.upper) == (self.lower, self.upper):
            #  ---      intersect
            #  ---      self
            return []
        elif ins.lower == self.lower:
            #  --       intersect
            #  ----     self
            return [Range(ins.upper, self.upper)]
        elif ins.upper == self.upper:
            #     --    intersect
            # ------    self
            return [Range(self.lower, ins.lower)]
        else:
            #   --      intersect
            #  ----     self
            return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]
    def add(self, offset):
        return Range(self.lower + offset, self.upper + offset)

class Map:
    def __init__(self, map_string):
        self.rules = []
        for line in map_string.splitlines()[1:]:
            destination, source, size = map(int, line.split())
            self.rules.append((destination, source, size))

    def convert(self, input):
        for destination, source, size in self.rules:
            if source <= input < source + size:
                return destination + input - source
        return input

class part2solver:
    def __init__(self, maps):
        self.maps = maps
        self.answer = float('inf')
    def propagate(self, r: Range, layer: int):
        if layer == len(self.maps):
            self.answer = min(self.answer, r.lower)
            return
        for destination, source, size in self.maps[layer].rules:
            map_r = Range(source, source + size)
            ins = r.intersection(map_r)
            if ins is not None:
                self.propagate(ins.add(destination - source), layer + 1)
                sub = r.subtract(map_r)
                if len(sub) == 0:
                    return
                r = sub[0]
                if len(sub) == 2:
                    self.propagate(sub[1], layer)
        self.propagate(r, layer + 1)

def getLocation(seed, maps):
    for m in maps:
        seed = m.convert(seed)
    return seed

def part1(input):
    seeds, *map_inputs = input.read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))
    maps = [Map(map_input) for map_input in map_inputs]
    locations = [getLocation(seed, maps) for seed in seeds]
    return min(locations)

def part2(input):
    seeds, *map_inputs = input.read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    maps = [Map(map_input) for map_input in map_inputs]
    par2answer = part2solver(maps)

    for i in range(0, len(seeds), 2):
        par2answer.propagate(Range(seeds[i], seeds[i] + seeds[i + 1]), 0)

    return par2answer.answer

print("Part 1: " + str(part1(open("inputs\day05.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day05.txt", "r"))))
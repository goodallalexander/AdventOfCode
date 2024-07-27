class Module:
    def __init__(self, line):
        name, destinations = line.split(" -> ")
        if name == "broadcaster":
            self.name = name
            self.type = 'B'
        else:
            self.name = name[1:]
            self.type = name[0]
        self.state = False
        self.destinations = destinations.split(", ")
        self.inputs = {}

class System:
    def __init__(self, input):
        self.modules = {module.name:module for module in map(Module, input.read().splitlines())}
        for empty in ("output", "rx"):
            self.modules[empty] = Module(empty + ' -> ')
            self.modules[empty].destinations = []
        for module in self.modules.values():
            for destination in module.destinations:
                self.modules[destination].inputs[module.name] = False

        self.parent ,= self.modules['rx'].inputs.keys()
        self.listen = {node:None for node in self.modules[self.parent].inputs.keys()}

        self.queue = []
        self.pulses = [0, 0]
        self.buttonPresses = 0
    
    def buttonPress(self):
        self.buttonPresses += 1
        self.queue = [("button", "broadcaster", False)]
        while self.queue:
            self.process(*self.queue.pop(0))

    def process(self, source, name, level):
        self.pulses[level] += 1
        module = self.modules[name]
        if module.type == "%":
            if level: return
            module.state = not module.state

        elif module.type == "&":
            module.inputs[source] = level
            module.state = not all(module.inputs.values())

            if name == self.parent:
                for key, value in self.listen.items():
                    if value is None and key == source and level:
                        self.listen[key] = self.buttonPresses

        for destination in module.destinations:
            self.queue.append((name, destination, module.state))

    def scorePart1(self):
        return self.pulses[0] * self.pulses[1]
    
    def scorePart2(self):
        answer = 1
        for value in self.listen.values():
            answer *= value
        return answer

def part1(input):
    system = System(input)
    for _ in range(1000):
        system.buttonPress()
    return system.scorePart1()

def part2(input):
    system = System(input)
    while None in system.listen.values():
        system.buttonPress()
    return system.scorePart2()

print("Part 1: " + str(part1(open("inputs\day20.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day20.txt", "r"))))
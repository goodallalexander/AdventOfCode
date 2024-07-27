import heapq

POINT = complex

class State:
    def __init__(self, loss, position, direction, continuousSteps):
        self.loss = loss
        self.position = position
        self.direction = direction
        self.continuousSteps = continuousSteps
        self.key = (self.position, self.direction, self.continuousSteps)
    def __lt__(self, other):
        return(self.loss, self.continuousSteps) < (other.loss, other.continuousSteps)
        

def part1(input):
    grid = {}
    for y, row in enumerate(input.read().splitlines()):
        for x, value in enumerate(row):
            grid[POINT(x, y)] = int(value)
    shape = len(SIZE)
    end = POINT(len(SIZE[0]) - 1, shape - 1)

    def solve():
        seen = set()
        Q = [State(0, 0, 1, 0), State(0, 0, 1j, 0)]
        while Q:
            state = heapq.heappop(Q)
            if state.key in seen:
                continue
            seen.add(state.key)

            if state.position == end:
                return state.loss

            if state.continuousSteps < 3 and state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, state.continuousSteps + 1))

            state.direction *= 1j

            if state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, 1))

            state.direction *= -1

            if state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, 1))

    return solve()

def part2(input):
    grid = {}
    for y, row in enumerate(input.read().splitlines()):
        for x, value in enumerate(row):
            grid[POINT(x, y)] = int(value)
    shape = len(SIZE)
    end = POINT(len(SIZE[0]) - 1, shape - 1)

    def solve():
        seen = set()
        Q = [State(0, 0, 1, 0), State(0, 0, 1j, 0)]
        while Q:
            state = heapq.heappop(Q)
            if state.key in seen:
                continue
            seen.add(state.key)

            if state.position == end and state.continuousSteps >= 4:
                return state.loss

            if state.continuousSteps < 10 and state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, state.continuousSteps + 1))

            state.direction *= 1j

            if 4 <= state.continuousSteps and state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, 1))

            state.direction *= -1

            if 4 <= state.continuousSteps and state.position + state.direction in grid:
                heapq.heappush(Q, State(state.loss + grid[state.position + state.direction], state.position + state.direction, state.direction, 1))

    return solve()


SIZE = open("inputs\day17.txt", "r").read().splitlines()

print("Part 1: " + str(part1(open("inputs\day17.txt", "r"))))
print("Part 2: " + str(part2(open("inputs\day17.txt", "r"))))
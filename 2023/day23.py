Point = complex

directions = (-1j, 1, 1j, -1)
slopes = dict(zip("^>v<", directions))

class Graph:
    def __init__(self, grid, start, end, part1):
        self.nodes = {}
        for point, value in grid.items():
            if value =='.':
                self.nodes[point] = Node(point)
            if value in slopes:
                self.nodes[point] = Node(point)
                if part1:
                    self.nodes[point].direction = slopes[value]

        self.start = self.nodes[start]
        self.end = self.nodes[end]

        for point, node in self.nodes.items():
            for direction in directions:
                if point + direction in self.nodes:
                    if self.nodes[point + direction].direction in (None, direction):
                        node.edges[self.nodes[point + direction]] = 1
        self.compress()

    def solve(self):
        answer = 0
        stack = [(self.start, 0, [])]
        while stack:
            node, distance, seen = stack.pop(-1)
            if node == self.end:
                answer = max(answer, distance)
            for edge in node.edges:
                if edge not in seen:
                    stack.append((edge, distance + node.edges[edge], seen + [edge]))

        return answer
    
    def compress(self):
        for node in self.nodes.values():
            if node.direction is not None :continue
            if len(node.edges) == 2 and not any(edge.direction for edge in node.edges):
                node1, node2 = node.edges.keys()
                del node1.edges[node]
                del node2.edges[node]
                node1.edges[node2] = sum(node.edges.values())
                node2.edges[node1] = sum(node.edges.values())


class Node:
    def __init__(self, position):
        self.position = position
        self.edges = {}
        self.direction = None

def part1(input):
    grid = {}
    for y, r in enumerate(input.splitlines()):
        for x, value in enumerate(r):
            grid[Point(x, y)] = value
            if y == 0 and value == '.':
                start = Point(x, y)
            if y == len(input.splitlines()) - 1 and value == '.':
                end = Point(x, y)

    return Graph(grid, start, end, True).solve()

def part2(input):
    grid = {}
    for y, r in enumerate(input.splitlines()):
        for x, value in enumerate(r):
            grid[Point(x, y)] = value
            if y == 0 and value == '.':
                start = Point(x, y)
            if y == len(input.splitlines()) - 1 and value == '.':
                end = Point(x, y)

    return Graph(grid, start, end, False).solve()

print("Part 1: " + str(part1(open("inputs\\day23.txt", "r").read())))
print("Part 2: " + str(part2(open("inputs\\day23.txt", "r").read())))
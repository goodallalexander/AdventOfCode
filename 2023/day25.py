from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.parent = {node:None for node in self.graph}
    def breadth_first_search(self, source, sink): #s source, t sink 
        self.parent = {node:None for node in self.graph}
        self.parent[source] = source
        queue = [source]
        while queue:
            node = queue.pop(0)
            for edge, capacity in self.graph[node].items():
                if capacity > 0 and self.parent[edge] is None:
                    self.parent[edge] = node
                    queue.append(edge)
        return self.parent[sink] is not None
    def minCut(self, source, sink):
        for value, edge in self.graph.items():
            for k in edge:
                self.graph[value][k] = 1
        maxFlow = 0
        while self.breadth_first_search(source, sink):
            flow = float('inf')
            node = sink
            while node != source:
                flow = min(flow, self.graph[self.parent[node]][node])
                node = self.parent[node]
            maxFlow += flow

            v = sink
            while v != source:
                u = self.parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = u
        return maxFlow
    def solve(self):
        graph = len({node for node, partent in self.parent.items() if partent})
        return (len(self.graph) - graph) * graph

def part1(input):
    graph = defaultdict(dict)
    for line in input.splitlines():
        leftHandSide, rightHandSide = line.split(": ")
        for component in rightHandSide.split():
            graph[leftHandSide][component] = 1
            graph[component][leftHandSide] = 1

    graph = Graph(graph)
    source, *other = graph.graph
    for sink in other:
        if graph.minCut(source, sink) == 3:
            break
    return graph.solve()

def part2(input):
    return "Merry Christmas!"

print("Part 1: " + str(part1(open("inputs\\day25.txt", "r").read())))
print("Part 2: " + str(part2(open("inputs\\day25.txt", "r").read())))
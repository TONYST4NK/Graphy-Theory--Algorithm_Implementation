from collections import defaultdict
import itertools
import math
import sys
import heapq


# Graph Class
class Graph:
    def __init__(self):
        self.edges = {}
        self.adj = defaultdict(list)

    def add_edge(self, edge_id, u, v, w):
        self.edges[edge_id] = (u, v, w)
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def degree(self, node):
        return len(self.adj[node])

    def summary(self):
        s = []
        s.append(f"Total vertices (unique seen): {len(self.adj)}")
        s.append(f"Total edges (counted by id): {len(self.edges)}")
        s.append("Edges (id: u <-> v, weight):")
        for edge_id, (u, v, w) in self.edges.items():
            s.append(f"  {edge_id}: {u} <-> {v}, cost={w}")
        s.append("Degrees:")
        for node in self.adj:
            s.append(f"  {node}: degree = {self.degree(node)}")
        return "\n".join(s)


# Dijkstra Shortest Path
def dijkstra(graph, start):
    dist = {node: math.inf for node in graph.adj}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


# Find Odd Degree Vertices
def find_odd_vertices(graph):
    return [node for node in graph.adj if graph.degree(node) % 2 == 1]


# Minimum Weight Matching
def min_weight_matching(odd_vertices, dist):
    min_pairing = None
    min_sum = math.inf

    for pairing in itertools.permutations(odd_vertices):
        valid = True
        total = 0
        for i in range(0, len(pairing), 2):
            u = pairing[i]
            v = pairing[i + 1]
            total += dist[u][v]
        if total < min_sum:
            min_sum = total
            min_pairing = pairing
    return min_sum, min_pairing


# CPP Solver
def chinese_postman(graph):
    total_edge_cost = sum(w for (_, _, w) in graph.edges.values())
    odd_vertices = find_odd_vertices(graph)

    print(f"\nOdd degree vertices: {odd_vertices}")
    if len(odd_vertices) == 0:
        print("Graph is Eulerian → no extra edges needed.")
        print(f"Minimum CPP cost = {total_edge_cost}")
        return total_edge_cost

    # Compute all-pairs shortest paths (for odd vertices)
    dist = {u: dijkstra(graph, u) for u in odd_vertices}

    # Find minimum weight perfect matching among odd vertices
    added_cost, pairing = min_weight_matching(odd_vertices, dist)

    print(f"Optimal matching pairs: {pairing}")
    print(f"Added cost to make Eulerian: {added_cost}")

    print(f"Minimum CPP cost = {total_edge_cost + added_cost}")
    return total_edge_cost + added_cost


# Input Reader
def read_input_stdin():
    data = sys.stdin.read().strip().split()
    it = iter(map(int, data))
    try:
        n = next(it)
        e = next(it)
    except StopIteration:
        raise SystemExit("Unexpected end of input while reading n or e.")

    g = Graph()
    for _ in range(e):
        try:
            edge_id = next(it)
            u = next(it)
            v = next(it)
            w = next(it)
        except StopIteration:
            raise SystemExit("Unexpected end of input while reading edges.")
        g.add_edge(edge_id, u, v, w)

    try:
        start = int(next(it))
    except StopIteration:
        raise SystemExit("Unexpected end of input while reading start node.")

    return n, e, g, start


# Main
if __name__ == "__main__":
    n, e, g, start = read_input_stdin()
    print("=== Parsed input ===")
    print(f"n (declared): {n}")
    print(f"e (declared): {e}")
    print(f"start node: {start}\n")
    print(g.summary())

    print("\n=== Solving Chinese Postman Problem ===")
    chinese_postman(g)


# Code Run
# python3 cpp_algorithm.py < input_sample.txt    
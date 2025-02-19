#task2lesson29.py


"""
    Using breadth-first search write an algorithm that can determine the shortest path 
    from each vertex to every other vertex. This is called the all-pairs shortest path problem.
"""


from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortest_path(self, start):
        # Initialize distances from the start vertex
        distances = [float('inf')] * self.V
        distances[start] = 0

        # Queue for BFS
        queue = deque([start])

        while queue:
            u = queue.popleft()

            # Explore all neighbors of u
            for v in self.graph[u]:
                if distances[v] == float('inf'):  # If v is not visited
                    distances[v] = distances[u] + 1
                    queue.append(v)

        return distances

    def all_pairs_shortest_path(self):
        # Initialize the distance matrix
        dist = [[float('inf')] * self.V for _ in range(self.V)]

        # Set diagonal to 0 (distance from a vertex to itself)
        for i in range(self.V):
            dist[i][i] = 0

        # Run BFS from each vertex to fill the distance matrix
        for u in range(self.V):
            distances_from_u = self.bfs_shortest_path(u)
            for v in range(self.V):
                dist[u][v] = distances_from_u[v]

        return dist


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    shortest_paths = g.all_pairs_shortest_path()

    print("All-Pairs Shortest Paths:")
    for row in shortest_paths:
        print(row)

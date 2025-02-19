#task1lesson29.py


"""
    Modify the 'depth-first search' to produce strongly connected components
"""


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)  # Push the node to the stack after finishing

    def reverse_graph(self):
        reversed_graph = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph

    def get_scc(self):
        stack = []
        visited = [False] * self.V

        # Step 1: Fill the stack based on finishing times
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 2: Reverse the graph
        reversed_graph = self.reverse_graph()

        # Step 3: Perform DFS on the reversed graph in stack order
        visited = [False] * self.V
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = []
                reversed_graph.dfs(node, visited, scc)
                sccs.append(scc)

        return sccs


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Strongly Connected Components:")
    print(g.get_scc())

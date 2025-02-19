
class Node:

    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return f"node={self.id}"

    # def __eq__(self, value):
    #     pass


class Graph:
    def __init__(self):
        self.node_list = []  # [1, 2, 3, 4, 5, 6]
        self.edge_list = []  # [(1, 2), (1, 3), ...]

    def find_node_by_id(self, node_id):
        for node in self.node_list:
            if node.id == node_id:
                return node
        return None

    def add_node(self, node_id, node_data=None):
        if self.find_node_by_id(node_id) is not None:
            raise Exception("Node already exists!")
        node = Node(node_id, node_data)
        self.node_list.append(node)

    def add_edge(self, node_id_a, node_id_b):
        node_a = self.find_node_by_id(node_id_a)
        node_b = self.find_node_by_id(node_id_b)
        if node_a is None or node_b is None:
            raise Exception("NO node was find")
        if node_a is node_b:
            raise Exception()
        self.edge_list.append((node_a, node_b))

    def remove_edge(self, node_id_a, node_id_b):
        node_a = self.find_node_by_id(node_id_a)
        node_b = self.find_node_by_id(node_id_b)
        if node_a is None or node_b is None:
            raise Exception("NO node was find")
        for idx, edge in enumerate(self.edge_list):
            if (edge[0] is node_a and edge[1] is node_b) or (edge[1] is node_a and edge[0] is node_b):
                self.edge_list.pop(idx) # self.edge_list.remove(edge)  
                del self.edge_list[idx]
                return True
        return False

    def remove_node(self, node_id):
        node = self.find_node_by_id(node_id)
        if node is None:
            raise Exception("NO node was find")
        remove_edges = []
        for edge in self.edge_list:
            if node.id == edge[0] or node.id == edge[1]:
                remove_edges.append(edge)
        while remove_edges:
            edge = remove_edges.pop()
            self.edge_list.remove(edge)
            del edge
        self.node_list.remove(node)

    def adjacent(self, node_id_a, node_id_b):
        node_a = self.find_node_by_id(node_id_a)
        node_b = self.find_node_by_id(node_id_b)
        if node_a is None or node_b is None:
            raise Exception("NO node was find")
        for edge in self.edge_list:
            if (edge[0] is node_a and edge[1] is node_b) or (edge[1] is node_a and edge[0] is node_b):
                return True
        return False
    
    def __str__(self):
        result = "Nodes [" + ', '.join(map(str, self.node_list)) + ']\n'
        result += "Edges [" + ', '.join(map(lambda edge: f"({str(edge[0])}, {str(edge[1])})", self.edge_list)) + ']\n'
        return result
    

if __name__ == '__main__':
    graph = Graph()

    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')


    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    # graph.add_edge('c', 'b')
    print(graph)

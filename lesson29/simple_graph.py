
class Node:

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.color = 0
        self.adjacent_nodes = set() 

    def __str__(self):
        return f"node={self.id}: color-{self.color}"

    # def __eq__(self, value):
    #     pass


class Graph:
    def __init__(self):
        self.nodes = {}  # {node.id: node}

    def find_node_by_id(self, node_id):
        return self.nodes.get(node_id)

    def add_node(self, node_id, node_data=None):
        if self.find_node_by_id(node_id) is not None:
            raise Exception("Node already exists!")
        node = Node(node_id, node_data)
        self.nodes[node_id] = node

    def add_edge(self, node_id_a, node_id_b):
        node_a = self.find_node_by_id(node_id_a)
        node_b = self.find_node_by_id(node_id_b)
        if node_a is None or node_b is None:
            raise Exception("NO node was find")
        if node_a is node_b:
            raise Exception()
        node_a.adjacent_nodes.add(node_b)
        node_b.adjacent_nodes.add(node_a)

    def dfs(self, start_node):
        
        # node = self.find_node_by_id(start_node_id)
        if start_node:
            if start_node.color == 1:
                return
            start_node.color = 1
            for adj_node in start_node.adjacent_nodes:
                self.dfs(adj_node)

    def paint_nodes_white(self):
        for node_id in self.nodes:
            node = self.nodes[node_id]
            node.color = 0

    def is_connected(self):
        result = True
        self.paint_nodes_white()
        for node in self.nodes.values():
            self.dfs(node)
            break

        for node in self.nodes.values():
            if node.color == 0:
                return False 
                break
        self.paint_nodes_white()
        return result 

    # def remove_edge(self, node_id_a, node_id_b):
    #     node_a = self.find_node_by_id(node_id_a)
    #     node_b = self.find_node_by_id(node_id_b)
    #     if node_a is None or node_b is None:
    #         raise Exception("NO node was find")
    #     for idx, edge in enumerate(self.edge_list):
    #         if (edge[0] is node_a and edge[1] is node_b) or (edge[1] is node_a and edge[0] is node_b):
    #             self.edge_list.pop(idx) # self.edge_list.remove(edge)  
    #             del self.edge_list[idx]
    #             return True
    #     return False

    # def remove_node(self, node_id):
    #     node = self.find_node_by_id(node_id)
    #     if node is None:
    #         raise Exception("NO node was find")
    #     remove_edges = []
    #     for edge in self.edge_list:
    #         if node.id == edge[0] or node.id == edge[1]:
    #             remove_edges.append(edge)
    #     while remove_edges:
    #         edge = remove_edges.pop()
    #         self.edge_list.remove(edge)
    #         del edge
    #     self.node_list.remove(node)

    # def adjacent(self, node_id_a, node_id_b):
    #     node_a = self.find_node_by_id(node_id_a)
    #     node_b = self.find_node_by_id(node_id_b)
    #     if node_a is None or node_b is None:
    #         raise Exception("NO node was find")
    #     for edge in self.edge_list:
    #         if (edge[0] is node_a and edge[1] is node_b) or (edge[1] is node_a and edge[0] is node_b):
    #             return True
    #     return False
    
    def __str__(self):
        result = "Nodes [" + ', '.join(map(str, self.nodes.values())) + ']'
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

    print(graph.is_connected())

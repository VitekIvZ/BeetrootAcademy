class BinaryTreeNode:
    def __init__(self, key, left_node=None, right_node=None):
        self.key = key
        self.left_node = left_node
        self.right_node = right_node

    def _gen(self):
        if self.left_node is not None:
            yield from self.left_node
        yield self
        if self.right_node is not None:
            yield from self.right_node
    
    def __iter__(self):
        self.gen = self._gen()
        return self
    
    def __next__(self):
        return next(self.gen)

    

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, key):
        def _add(key, node):
            if node is None:
                return BinaryTreeNode(key)
            if node.key >= key:
                node.left_node = _add(key, node.left_node)
            else:
                node.right_node = _add(key, node.right_node)
            return node
        
        self.root = _add(key, self.root)

    def __str__(self):
        def bfs(node_list):
            result = ""
            if len(node_list) == 0:
                return result
            next_level = []
            for node in node_list:
                if node is not None:
                    result += str(node.key)+"\t"
                    next_level.append(node.left_node)
                    next_level.append(node.right_node)
            result += "\n" + bfs(next_level)
            return result
        return bfs([self.root])

    def __iter__(self):
        self.it = iter(self.root)
        return self
    
    def __next__(self):
        return next(self.it)
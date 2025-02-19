
from nodes import NodeII


class Deque:

    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.__size = 0

    def put_right(self, node: NodeII):
        if self.last_node:
            self.last_node.next_node = node
        self.last_node = node
        self.__size += 1
        if not self.first_node:
            self.first_node = node

    def put_left(self, node: NodeII):
        if self.first_node:
            self.first_node.prev_node = node
        self.first_node = node
        self.__size += 1
        if not self.last_node:
            self.last_node = node

    def get_left(self):        
        if self.first_node:
            node = self.first_node
            self.first_node = node.next_node
            node.next_node = None
            self.__size -= 1
            return node
        return None
    
    def get_right(self):        
        if self.last_node:
            node = self.last_node
            self.last_node = node.prev_node
            node.prev_node = None
            self.__size -= 1
            return node
        return None

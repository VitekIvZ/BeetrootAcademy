from time import time
from queue import Queue

from nodes import Node


class QueueF:

    def __init__(self, first_node=None, last_node=None):
        self.first_node = None
        self.last_node = None
        self.__size = 0
        self.indexex = None

    def indexing(self):
        if self.__size:
            self.indexex = [None for _ in range(self.size)]
        current_node = self.first_node
        for _ in range(self.size):
            self.indexex = current_node 
            current_node = current_node.next_node

    def put(self, node: Node):
        if self.last_node:
            self.last_node.next_node = node
        self.last_node = node
        self.__size += 1
        if not self.first_node:
            self.first_node = node

    def get(self):        
        if self.first_node:
            node = self.first_node
            self.first_node = node.next_node
            node.next_node = None
            self.__size -= 1
            return node
        return None
    
    def __getitem__(self, idx):   #  O(n)
        current_node = self.first_node
        if self.indexex:
            return self.indexex[idx]
        for _ in range(idx-1):
            current_node = current_node.next_node 
        return current_node
    
    @property
    def size(self):
        return self.__size
    
    def from_list(self, lst: list):
        pass

    def display(self):
        current_node = self.first_node
        while current_node is not self.last_node:
            print(f"node: data = {current_node.get_data()}")
            current_node = current_node.next_node
        print(f"node: data = {current_node.get_data()}")


if __name__ == '__main__':
    # count of elements
    N = 100
    lst = [Node(i) for i in range(N)]

    que = QueueF()
    for i in range(N):
        que.put(Node(i+1))

    print(que[50].get_data())

    queue = Queue()
    for i in range(N):
        queue.put(Node(i))

    # start_lst = time()
    # for _ in range(100*N):
    #     lst.insert(0, lst.pop())
    # print(f"list manipulation time = {time() - start_lst:.3f}")
    # # que.display()

    # start_que = time()
    # for _ in range(100*N):
    #     que.put(que.get())
    # print(f"queue manipulation time = {time() - start_que:.3f}")

    # start_queue = time()
    # for _ in range(100*N):
    #     node = queue.get()
    #     queue.put(node)
    # print(f"standart queue manipulation time = {time() - start_queue:.3f}")

    
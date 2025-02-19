#task3lesson25.py


"""
    Implement a queue using a singly linked list.
"""


from nodes import Node 


class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.__size = 0

    def is_empty(self):
        return self.first_node is None
    
    @property
    def size(self):
        return self.__size

    def put(self, item):
        new_node = Node(item)
        if self.last_node:
            self.last_node.next_node = new_node
        self.last_node = new_node
        if not self.first_node:
            self.first_node = new_node
        self.__size += 1

    def get(self):   
        if self.is_empty():
            raise IndexError("dequeue from empty queue")     
        node = self.first_node
        self.first_node = node.next_node
        if not self.first_node:
            self.last_node = None
        self.__size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.first_node.data

    def __str__(self):
        current = self.first_node
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return " -> ".join(elements) + " -> None"

def main():
    queue = Queue()
    for i in range(1, 5):
        queue.put(i)
    
    print("Queue after adding elements:")
    print(queue)

    print(f"First element: {queue.peek()}")
    print(f"Removed element: {queue.get()}")
    print("Queue after removing element:")
    print(queue)

    print(f"Queue size: {queue.size}")        

if __name__ == "__main__":
    main()
    

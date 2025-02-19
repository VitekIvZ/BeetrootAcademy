#task2lesson25.py


"""
    Implement a stack using a singly linked list.
"""


from nodes import Node 


class Stack:
    def __init__(self):
        self.last = None
        self.__size = 0

    def is_empty(self):
        return self.last is None
    
    @property
    def size(self):
        return self.__size

    def push(self, item):
        new_node = Node(item, self.last)
        self.last = new_node
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.last.data
        self.last = self.last.next_node
        self.__size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.last.data

    def __str__(self):
        current = self.last
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return " -> ".join(elements) + " -> None"

def main():    
    stack = Stack()
    for i in range(1, 5):
        stack.push(i)
    
    print("Stack after adding elements:")
    print(stack)

    print(f"Last element: {stack.peek()}")
    print(f"Popped element: {stack.pop()}")
    print("Stack after popping element:")
    print(stack)

    print(f"Stack size: {stack.size}")

if __name__ == "__main__":
    main()

#task3lesson24.py


"""
Extend the Stack to include a method called get_from_stack that searches and returns an element 
e from a stack. Any other element must remain on the stack respecting their order. 
Consider the case in which the element is not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that searches and returns an element e 
from a queue. Any other element must remain in the queue respecting their order. Consider the case 
in which the element is not found - raise ValueError with proper info Message
"""
    
    
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        temp_stack = Stack()
        found = False

        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            else:
                temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Element {e} not found in stack")

        return e
    
    
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

    def get_from_queue(self, e):
        temp_queue = Queue()
        found = False

        while not self.is_empty():
            item = self.dequeue()
            if item == e:
                found = True
                break
            else:
                temp_queue.enqueue(item)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        if not found:
            raise ValueError(f"Element {e} not found in queue")

        return e


def test_Stack():
    stack = Stack()
    for i in range(1, 5):
        stack.push(i)
    
    try:
        print(f"Element found: {stack.get_from_stack(3)}")
        print(f"Stack after removal: {stack.items}")
    except ValueError as ve:
        print(ve)

        
def test_Queue():
    queue = Queue()
    for i in range(1, 5):
        queue.enqueue(i)
    
    try:
        print(f"Element found: {queue.get_from_queue(3)}")
        print(f"Queue after removal: {queue.items}")
    except ValueError as ve:
        print(ve)  

    
if __name__ == "__main__":
    test_Stack()
    test_Queue()
    
    
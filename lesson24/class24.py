class Node:

    def __init__(self, data=None, next_node=None):
        self.next_node = next_node
        self.set_data(data)
        #self.__data = data
    
    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data
        

class Stack:
    def __init__(self):
        self.top = None

    def put(self, node: Node):
        node.next = self.top
        self.top = node

    def get(self) -> Node:
        if self.top is None:
            raise IndexError("get from empty stack")
        node = self.top
        self.top = self.top.next
        return node
    
    def display(self):
        current = self.top
        while current:
            print(current.get_data(), end=" -> ")
            current = current.next
        print("None")

    

if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.put(Node(i))
    
    print("Stack after adding elements:")
    stack.display()

    print(f"Element removed: {stack.get().get_data()}")

    print("Stack after removing element:")
    stack.display()
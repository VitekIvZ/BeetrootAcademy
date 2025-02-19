#task1lesson25.py


"""
    Extend UnsortedList

Implement append, index, pop, insert methods for UnsortedList. 
Also implement a slice method, which will take two parameters 'start' and 'stop', 
and return a copy of the list starting at the position and going up to but not including 
the stop position.
"""


from nodes import Node 


class UnsortedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def index(self, item):
        current = self.head
        position = 0
        while current:
            if current.data == item:
                return position
            current = current.next_node
            position += 1
        raise ValueError(f"{item} is not in the list")

    def pop(self, position=None):
        if self.head is None:
            raise IndexError("pop from empty list")

        if position is None:
            current = self.head
            if current.next_node is None:
                popped_data = current.data
                self.head = None
                return popped_data
            while current.next_node.next_node:
                current = current.next_node
            popped_data = current.next_node.data
            current.next_node = None
            return popped_data

        if position == 0:
            popped_data = self.head.data
            self.head = self.head.next_node
            return popped_data

        current = self.head
        prev = None
        current_position = 0
        while current and current_position < position:
            prev = current
            current = current.next_node
            current_position += 1

        if current is None:
            raise IndexError("pop index out of range")

        prev.next_node = current.next_node
        return current.data

    def insert(self, position, item):
        new_node = Node(item)
        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        current_position = 0
        while current and current_position < position:
            prev = current
            current = current.next_node
            current_position += 1

        if current_position != position:
            raise IndexError("insert index out of range")

        new_node.next_node = current
        prev.next_node = new_node

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start >= stop:
            raise ValueError("Invalid start or stop values")

        current = self.head
        current_position = 0
        new_list = UnsortedList()

        while current and current_position < stop:
            if current_position >= start:
                new_list.append(current.data)
            current = current.next_node
            current_position += 1

        return new_list

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return " -> ".join(elements) + " -> None"

def main():
    ul = UnsortedList()
    for i in range(1, 6):
        ul.append(i)

    print("Original list:")
    print(ul)

    print(f"Index of 3: {ul.index(3)}")

    print(f"Popped element: {ul.pop()}")
    print("List after pop:")
    print(ul)

    ul.insert(2, 10)
    print("List after inserting 10 at position 2:")
    print(ul)

    sliced_list = ul.slice(1, 3)
    print("Sliced list from position 1 to 3:")
    print(sliced_list)

if __name__ == "__main__":
    main()



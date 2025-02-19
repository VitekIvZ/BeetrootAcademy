from node import Node


class UnsortedDList:

    def __init__(self):
        self._head = None
        self._tail = None
        self.__size = 0

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        if self._head is not None:
            self._head.set_prev(temp)
        else:
            self._tail = temp
        self._head = temp
        self.__size += 1

    def add_tail(self, item):
        temp = Node(item)
        temp.set_prev(self._tail)
        if self._tail is not None:
            self._tail.set_next(temp)
        self._tail = temp
        self.__size += 1

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return current
    
    def search_from_tail(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return current
    
    def is_item(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        # previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                # previous = current
                current = current.get_next()

        self.__size -= 1

        if current is self._head:
            next_node = current.get_next()
            if current is not self._tail:
                next_node.set_prev(None)
            self._head = next_node
            return
        
        if current is self._tail:
            prev_node = current.get_prev()
            prev_node.set_next(None)
            self._tail = prev_node
            return

        prev_node = current.get_prev()
        next_node = current.get_next()
        prev_node.set_next(next_node)
        next_node.set_prev(prev_node)

    def __getitem__(self, idx):
        # curr_idx = 1
        if 0 < idx < self.__size+1:
            current = self._head
            for _ in range(1, idx):
                current = current.get_next()
            return current
        else:
            raise IndexError("!!!!")

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    
if __name__ == "__main__":
    my_list = UnsortedDList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)


    print(my_list[4].get_data())

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))

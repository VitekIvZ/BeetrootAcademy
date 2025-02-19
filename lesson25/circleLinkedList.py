from node import Node


class CircleLinkedList:

    def __init__(self):
        self._last = None
        self.__size = 0

    def is_empty(self):
        return self._last is None
    
    def add_first(self, item):
        temp = Node(item)
        if self._last is not None:
            first = self._last.get_next()
            temp.set_next(first)
            self._last.set_next(temp)
        else:
            self._last = temp
            self._last.set_next(temp)
        self.__size += 1

    # TODO: Implement!!!
    # def add_past(self, item):
    
    #     temp = Node(item)
    #     if self._last is not None:
    #         first = self._last.get_next()
    #         temp.set_next(first)
    #         self._last.set_next(temp)
    #     else:
    #         self._last = temp
    #         self._last.set_next(temp)
    #     self.__size += 1

    def __repr__(self):
        representation = "<CircularLinkedList: "
        current = self._last.get_next()
        while current is not self._last:
            representation += f"{current.get_data()} "
            current = current.get_next()
        representation += f"{current.get_data()} "
        return representation + ">"
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, new_size):
        self.__size = new_size


class JosephCircleLinkedList(CircleLinkedList):

    def kill_every(self, k):
        current = self._last
        while self.size > 1:
            for _ in range(k-1):
                current = current.get_next()
            node_to_remove = current.get_next()
            current.set_next(node_to_remove.get_next())
            self.dec_size()
        return current
    
    def get_last(self, k):
        return self.kill_every(k=k).get_data()
    
    def dec_size(self):
        self.size -= 1
        
    

if __name__ == "__main__":
    jos_list = JosephCircleLinkedList()

    # my_list.add_first(31)
    # my_list.add_first(77)
    # my_list.add_first(17)
    # my_list.add_first(93)
    # my_list.add_first(26)
    # my_list.add_first(54)

    for i in range(41, 0, -1):
        jos_list.add_first(i)

    print(jos_list)

    print(jos_list.get_last(3))



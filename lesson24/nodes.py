
class Node:

    def __init__(self, data=None, next_node=None):
        self.next_node = next_node
        self.set_data(data)
        #self.__data = data
    
    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data



class BinaryTree:

    def __init__(self, value=None):
        self.value =  value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            tr = BinaryTree(value)
            tr.left_child = self.left_child
            self.left_child = tr

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            tr = BinaryTree(value)
            tr.right_child = self.right_child
            self.right_child = tr

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def get_root_value(self):
        return self.value
    
    def set_root_value(self, value):
        self.value = value

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value, end=' ')
        if self.right_child:
            self.right_child.in_order()
        # print()

    def display(self, indent=0, symbol=' '):
        # print(f"{symbol*indent}{self.value}")
        text = f"{symbol*indent}{self.value}\n"
        text_left = ''
        if self.left_child:
            text_left = self.left_child.display(indent=indent+4, symbol=' ')
        text_right = ''
        if self.right_child:
            text_right = self.right_child.display(indent=indent+4, symbol=' ')
        return text + text_left + text_right

    def __repr__(self):
        return f"BinaryTree: {self.value}"

    def __str__(self):
        return self.display(indent=0, symbol=' ')
    

if __name__ == '__main__':
    tree = BinaryTree('a')

    tree.insert_left('b')
    left = tree.get_left_child()
    left.insert_left('d')
    left.insert_right('h')
    tree.insert_right('c')
    right = tree.get_right_child()
    right.insert_left('f')
    right.insert_right('g')

    print(tree)

    tree.in_order()
    print()
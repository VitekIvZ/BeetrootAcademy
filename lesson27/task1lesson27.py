#task1lesson27.py


"""
    Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та 
    видалення піддерева з дерева, що існує.
"""

class BinaryTree:
    def __init__(self, value=None):
        self.value = value
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

    def display(self, indent=0, symbol=' '):
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

    def insert_tree(self, tree, side='left'):
        """
        Вставляє дерево як ліве або праве піддерево.
        :param tree: BinaryTree, дерево для вставки
        :param side: str, 'left' або 'right', вказує, куди вставити дерево
        """
        if side == 'left':
            self.left_child = tree
        elif side == 'right':
            self.right_child = tree
        else:
            raise ValueError("Side must be 'left' or 'right'")
        
    def insert_tree_with_preservation(self, tree, side='left', attach_side='right'):
        if side not in ['left', 'right']:
            raise ValueError("Side must be 'left' or 'right'")
        if attach_side not in ['left', 'right']:
            raise ValueError("Attach side must be 'left' or 'right'")

        if side == 'left':
            if self.left_child:
            # Приєднуємо нове дерево до дітей існуючого лівого піддерева
                if attach_side == 'left':
                    if self.left_child.left_child is None:
                        self.left_child.left_child = tree  # Додаємо нове дерево до лівого піддерева
                    else:
                        self.left_child.left_child.insert_tree_with_preservation(tree, side='left', attach_side='left')
                else:
                    if self.left_child.right_child is None:
                        self.left_child.right_child = tree  # Додаємо нове дерево до правого піддерева
                    else:
                        self.left_child.right_child.insert_tree_with_preservation(tree, side='right', attach_side='left')
            else:
                self.left_child = tree  # Вставляємо нове дерево, якщо лівого немає
        elif side == 'right':
            if self.right_child:
            # Приєднуємо нове дерево до дітей існуючого правого піддерева
                if attach_side == 'left':
                    if self.right_child.left_child is None:
                        self.right_child.left_child = tree  # Додаємо нове дерево до лівого піддерева
                    else:
                        self.right_child.left_child.insert_tree_with_preservation(tree, side='left', attach_side='left')
                else:
                    if self.right_child.right_child is None:
                        self.right_child.right_child = tree  # Додаємо нове дерево до правого піддерева
                    else:
                        self.right_child.right_child.insert_tree_with_preservation(tree, side='right', attach_side='right')
            else:
                self.right_child = tree  # Вставляємо нове дерево, якщо правого немає

    def delete_subtree(self, side):
        """
        Видаляє ліве або праве піддерево.
        :param side: str, 'left' або 'right', вказує, яке піддерево видалити
        """
        if side == 'left':
            self.left_child = None
        elif side == 'right':
            self.right_child = None
        else:
            raise ValueError("Side must be 'left' or 'right'")


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

    print("Початкове дерево:")
    print(tree)

    print("In-order обхід:")
    tree.in_order()
    print()

    # Вставка нового дерева як лівого піддерева
    tree2 = BinaryTree('x')
    tree2.insert_left('y')
    tree2.insert_right('z')
    tree.insert_tree(tree2, side='left')

    print("\nДерево після вставки нового дерева як лівого піддерева:")
    print(tree)
    
    # Створюємо нове піддерево для вставки
    tree3 = BinaryTree('k')
    tree3.insert_left('l')
    tree3.insert_right('m')

    # Вставляємо нове піддерево як ліве піддерево зі збереженням попереднього
    tree.insert_tree_with_preservation(tree3, side='left')

    print("\nДерево після вставки нового піддерева зі збереженням попереднього:")
    print(tree)

    # Видалення правого піддерева
    tree.delete_subtree(side='right')

    print("\nДерево після видалення правого піддерева:")
    print(tree)
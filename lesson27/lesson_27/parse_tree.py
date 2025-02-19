import operator

from binary_tree import BinaryTree

class Stack:

    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container
    
    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()
    
    def __repr__(self):
        return self._container
    

class ParseTree:
    def __init__(self, math_exp=''):
        self.exp = math_exp
        self.stack = Stack()
        self._tree = tree = BinaryTree()
        self.stack.push(tree)
        if math_exp:
            self.parse()

    @property
    def tree(self):
        return self._tree

    def parse(self):
        # ( ( 7 + 3 ) * ( 5 - 2 ) )
        current_tree = self._tree
        token_list = self.exp.split()
        for token in token_list:
            if token == '(':
                current_tree.insert_left('')
                self.stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif token in {'+', '-', '*', '/'}:
                current_tree.set_root_value(token)
                current_tree.insert_right('')
                self.stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif token == ')':
                current_tree = self.stack.pop()

            else:
                current_tree.set_root_value(int(token))
                current_tree = self.stack.pop()

    def eval(self, exp=None):
        operators = {'+': operator.add, 
                     '-': operator.sub, 
                     '*': operator.mul, 
                     '/': operator.truediv}
        tree = exp if exp else self._tree
        left_exp = tree.get_left_child()
        right_exp = tree.get_right_child()
        if left_exp and right_exp:
            fn = operators[tree.get_root_value()]
            return fn(self.eval(left_exp), self.eval(right_exp))
        else:
            return tree.get_root_value()
        
    def _get_exp(self, tree=None):
        text = ''
        if tree:
            text = '(' + self._get_exp(tree.get_left_child())
            text += str(tree.get_root_value())
            text += self._get_exp(tree.get_right_child()) + ')'
        return text
    
    def print_exp(self, tree=None):
        curr_tree = tree if tree else self._tree
        return self._get_exp(curr_tree)


if __name__ == '__main__':

    pt = ParseTree("( ( 7 + 3 ) * ( 5 - 2 ) )")
    # pt.parse()
    print(pt.tree)
    print(pt.print_exp())
    print(pt.eval())
                
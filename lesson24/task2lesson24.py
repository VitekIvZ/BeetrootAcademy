#task2lesson24.py

"""
    Write a program that reads in a sequence of characters, and determines whether it's parentheses, 
    braces, and curly brackets are "balanced."
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

def is_balanced(sequence):
    stack = Stack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    opening_brackets = matching_brackets.values()

    for char in sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in matching_brackets:
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")
    if is_balanced(sequence):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")

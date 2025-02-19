# mymod.py

import sys


def count_lines(name):
    """Counts the number of lines in the specified file."""
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    """Counts the number of characters in the specified file."""
    with open(name, 'r') as file:
        content = file.read()
        return len(content)


def test(name):
    """Calls both counting functions and prints the results."""
    lines = count_lines(name)
    chars = count_chars(name)
    return lines, chars
 
    
if __name__ == "__main__":
    
    if len(sys.argv) > 1:
            name = str(sys.argv[1])  
    else:
            name = input("Enter name of file: ")        
    
    lines, chars = test(name)
    
    print(f"File: {name}\nLines: {lines}\nCharacters: {chars}")

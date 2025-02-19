#task3lesson21.py


"""
    Pytest fixtures with context manager

Create a simple function, which performs any logic of your choice with text data, 
which it obtains from a file object, passed to this function ( def test(file_obj) ). 

Create a test case for this function using pytest library (Full pytest documentation). 

Create pytest fixture, which uses your implementation of the context manager to return a file object, 
which could be used inside your function.
"""


import os
import sys
sys.path.append("./lesson21")
from task1lesson21 import FileContextManager

def process_file(file_obj):
    content = file_obj.read()
    return content.upper()


if __name__ == "__main__":
    file_path = "./lesson21/test.txt"
    
    with open(file_path, 'w') as f:
        f.write("Hello, world!")

    with FileContextManager(file_path, 'r') as f:
        result = process_file(f)
        print(result)

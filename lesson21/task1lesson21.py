#task1lesson21.py


"""
    File Context Manager class

Create your own class, which can behave like a built-in function 'open'. 
Also, you need to extend its functionality with counter and logging. 
Pay special attention to the implementation of '__exit__' method, which has to cover all 
the requirements to context managers mentioned here:
"""


import os

class FileContextManager:
    counter = 0

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        FileContextManager.counter += 1
        self.file = open(self.file_name, self.mode)
        print(f"Opening file: {self.file_name}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closing file: {self.file_name}")
        if exc_type:
            print(f"An exception occurred: {exc_type}, {exc_value}")
        return False  


if __name__ == "__main__":
    file_path = "./lesson21/test.txt"
        
    with open(file_path, 'w') as f:
        f.write("Hello, world!")

    with FileContextManager(file_path, 'r') as f:
        content = f.read()
        print(content)

    print(f"File opened {FileContextManager.counter} times.")
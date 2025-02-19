#task2lesson21.py


"""
    Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything 
works as designed. And also, write tests when your class raises errors or you have errors in the 
runtime context suite.
"""


import unittest
import os
import sys
sys.path.append("./lesson21")
from task1lesson21 import FileContextManager

class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "./lesson21/test.txt"
        with open(self.test_file, 'w') as f:
            f.write("Hello, world!")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_open_and_read(self):
        with FileContextManager(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Hello, world!")
        self.assertEqual(FileContextManager.counter, 1)

    def test_file_open_and_write(self):
        with FileContextManager(self.test_file, 'w') as f:
            f.write("New content")
        with FileContextManager(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "New content")
        self.assertEqual(FileContextManager.counter, 3)  

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("/non/existent/file.txt", 'r') as f:
                pass

    def test_exception_handling(self):
        try:
            with FileContextManager(self.test_file, 'r') as f:
                raise ValueError("Test exception")
        except ValueError as e:
            self.assertEqual(str(e), "Test exception")
        self.assertEqual(FileContextManager.counter, 1)

if __name__ == "__main__":
    unittest.main()

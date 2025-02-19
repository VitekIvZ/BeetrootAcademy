#task3lesson21test.py


import pytest
import os
import sys
sys.path.append("./lesson21")
from task3lesson21 import process_file
from task1lesson21 import FileContextManager

@pytest.fixture
def file_obj():
    file_path = "./lesson21/test.txt"
    with open(file_path, 'w') as f:
        f.write("Hello, world!")
    with FileContextManager(file_path, 'r') as f:
        yield f

def test_process_file(file_obj):
    result = process_file(file_obj)
    assert result == "HELLO, WORLD!"

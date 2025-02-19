#task1lesson19.py


"""
    Create your own implementation of a built-in function enumerate, named 'with_index', 
    which takes two parameters: 'iterable' and 'start', default is 0. 
    Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


def test(data):
    data = list(data)
    for index, value in with_index(data, start=1):
        print(index, value)

if __name__ == "__main__":
    data = ['a', 'b', 'c', 'd']
    test(data)
    
    data = "Python"
    test(data)
    

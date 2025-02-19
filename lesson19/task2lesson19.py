#task2lesson19.py


"""
Create your own implementation of a built-in function range, named in_range(), 
which takes three parameters: 'start', 'end', and optional step. 
Tips: See the documentation for 'range' function 
"""


def in_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError("step argument must not be zero")
    
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step


def test():
    assert list(in_range(5)) == [0, 1, 2, 3, 4]
    assert list(in_range(1, 5)) ==  [1, 2, 3, 4]
    assert list(in_range(1, 10, 2)) == [1, 3, 5, 7, 9]
    assert list(in_range(10, 1, -2)) == [10, 8, 6, 4, 2]
    assert list(in_range(10, 1, 2)) == []
    
    print("All tests passed successfully!")
    
    
if __name__ == "__main__":
    test()
    
    
    
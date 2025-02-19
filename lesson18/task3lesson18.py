#task3lesson18.py


"""
    Write a class TypeDecorators which has several methods for converting results of functions 
    to a specified type (if it's possible):

methods:

to_int

to_str

to_bool

to_float

 

Don't forget to use @wraps

'''

class TypeDecorators:

    pass

 

@TypeDecorators.to_int

def do_nothing(string: str):

    return string

 

@TypeDecorators.to_bool

def do_something(string: str):

    return string

 

assert do_nothing('25') == 25

assert do_something('True') is True

'''
"""


from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to int")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to float")
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_float_example(string: str):
    return string


@TypeDecorators.to_str
def do_str_example(string: str):
    return string


def test():
    assert do_nothing('25') == 25
    assert do_something('True') is True
    assert do_float_example('25.5') == 25.5
    assert do_str_example('Python') == 'Python'


if __name__ == "__main__":
    test()
    
    print(do_nothing.__name__, do_nothing('25')) 
    print(do_something.__name__, do_something('True'))  
    print(do_float_example.__name__, do_float_example('25.5'))
    print(do_str_example.__name__, do_str_example('Python'))
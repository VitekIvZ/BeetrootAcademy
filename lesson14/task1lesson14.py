#task1lesson14.py

"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!
"""

def logger(func):
    def wrapper(*args):
        print(f"Function '{func.__name__}' called with arguments: {args} ")
        # Не виконуємо функцію, просто повертаємо None
        return None
    return wrapper


@logger
def add_function(a, b):
    return a + b


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

if __name__ == "__main__":
    add_function(4, 5)
    square_all(4, 5)
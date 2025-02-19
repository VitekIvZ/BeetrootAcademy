from time import time
from timeit import timeit
from functools import wraps, cache


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: runtime: {time() - start:8.5}")
        return result
    return wrapper


def p_tag(func):
    def wrapper(text):
        return "<p>{0}</p>".format(func(text))
    return wrapper


def tags(tag_name):
    def tag_decorator(func):
        def func_wrapper(text):
            return "<{0}>{1}</{0}>".format(tag_name, func(text))
        return func_wrapper
    return tag_decorator


def call_logger(func):
    count = 0
    def wrapper(arg):
        nonlocal count
        count += 1
        print(f"{count:>3} call {func.__name__} ({arg})")
        # result = func(arg)
        return func(arg)
    return wrapper


def custom_cache(func):
    cache = {}
    def wrapper(arg):
        if arg in cache:
            return cache[arg]
        result = func(arg)
        cache[arg] = result
        return result
    return wrapper


@p_tag
@tags("div")
def get_text(text):
    return f"This func inserts {text}..."


@timer
@tags("h1")
@tags("div")
@tags("p")
def add_text(text):
    return f"This func inserts {text}..."


# @timer
# @call_logger
# @custom_cache
@cache
def fib(n):
    """
    docs
    """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

def fibonacci(n):
    prev, curr = 0, 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for _ in range(1, n):
            prev, curr = curr, curr + prev
        return curr

 
if __name__ == '__main__':
    # fib_time = timer(fib)
    # print(fib(6))

    setup_string = """
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
"""

    print(fib(6), fibonacci(6))
    # get_text_obj = tags("div")(add_text)  # tag_decorator
    # print(add_text("Eurica!!!"))
    print(timeit("fib(20)", globals=globals(), number=1000))
    print(timeit("fibonacci(20)", globals=globals(), number=1000))
    print(timeit("fib(20)", setup=setup_string, number=1000))

#task1lesson13.py

"""
Write a Python program to detect the number of local variables declared in a function.
"""

def sample_function():
    a = 10
    b = 20
    c = 30
    d = 40

def count_local_variables(func):
    return func.__code__.co_nlocals

if __name__ == "__main__":
    num_locals = count_local_variables(sample_function)
    print(f"Number of local variables in 'sample_function': {num_locals}")
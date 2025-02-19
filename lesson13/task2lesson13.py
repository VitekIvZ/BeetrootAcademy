#task2lesson13.py

"""
Write a Python program to access a function inside a function 
(Tips: use function, which returns another function)
"""

def first_function():
    def second_function():
        return "Hello from the second function!"
    
    return second_function


if __name__ == "__main__":

    returned_function = first_function()
    print(returned_function())  

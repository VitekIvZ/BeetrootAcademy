#task9_1-2.py

from task9_1_1 import add_numbers


def new_add_numbers(num1, num2):
    result = add_numbers(num1, num2)
    return result
    

if __name__ == "__main__":
    
    result = new_add_numbers(16, 27)
    print(result)
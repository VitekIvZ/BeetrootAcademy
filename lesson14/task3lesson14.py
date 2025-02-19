#task2lesson14.py

"""
Write a decorator 'arg_rules' that validates arguments passed to the function.

A decorator should take 3 arguments:

    max_length: 15
    type_: str
    contains: []  - list of symbols that an argument should contain

 

If some of the rules' checks returns False, the function should return False 
and print the reason it failed; otherwise, return the result.

"""


# task3lesson14.py

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            # Перевірка типу аргументу
            if not isinstance(arg, type_):
                print(f"Argument type is not {type_.__name__}")
                return False
            
            # Перевірка довжини аргументу
            if len(arg) > max_length:
                print(f"Argument length is greater than {max_length}")
                return False
            
            # Перевірка наявності символів у аргументі
            for symbol in contains:
                if symbol not in arg:
                    print(f"Argument does not contain required symbol: {symbol}")
                    return False
            
            return func(arg)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


def test_func():
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'


if __name__ == "__main__":
    test_func()
    

    



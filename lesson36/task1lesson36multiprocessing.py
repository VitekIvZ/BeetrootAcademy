#task1lesson36.py


"""
Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an 
input number. Schedule the execution of this code using asyncio.gather for a list of integers from 1 
to 10. You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
Time the execution of both realizations, explore the results, what realization is more effective, why 
did you get a result like this.
"""


import multiprocessing
import time

# Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Square function
def square(n):
    return n * n

# Cube function
def cube(n):
    return n * n * n

# Main function to calculate results using multiprocessing
def main():
    numbers = list(range(1, 11))
    
    with multiprocessing.Pool() as pool:
        fib_results = pool.map(fibonacci, numbers)
        fact_results = pool.map(factorial, numbers)
        sq_results = pool.map(square, numbers)
        cube_results = pool.map(cube, numbers)
    
    return fib_results, fact_results, sq_results, cube_results

if __name__ == "__main__":
    start_time = time.time()
    fib_results, fact_results, sq_results, cube_results = main()
    end_time = time.time()
    
    print("Fibonacci Results:", fib_results)
    print("Factorial Results:", fact_results)
    print("Square Results:", sq_results)
    print("Cube Results:", cube_results)
    print(f"Multiprocessing Execution Time: {end_time - start_time:.4f} seconds")
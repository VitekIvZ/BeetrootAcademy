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


import asyncio

# Asynchronous Fibonacci function
async def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Asynchronous Factorial function
async def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Asynchronous Square function
async def square(n):
    return n * n

# Asynchronous Cube function
async def cube(n):
    return n * n * n

# Main asynchronous function to gather results
async def main():
    numbers = list(range(1, 11))
    
    # Schedule all tasks
    fib_results = await asyncio.gather(*[fibonacci(n) for n in numbers])
    fact_results = await asyncio.gather(*[factorial(n) for n in numbers])
    sq_results = await asyncio.gather(*[square(n) for n in numbers])
    cube_results = await asyncio.gather(*[cube(n) for n in numbers])
    
    return fib_results, fact_results, sq_results, cube_results


if __name__ == "__main__":
    import time
    start_time = time.time()
    fib_results, fact_results, sq_results, cube_results = asyncio.run(main())
    end_time = time.time()
    
    print("Fibonacci Results:", fib_results)
    print("Factorial Results:", fact_results)
    print("Square Results:", sq_results)
    print("Cube Results:", cube_results)
    print(f"Asynchronous Execution Time: {end_time - start_time:.4f} seconds")

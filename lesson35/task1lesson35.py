#task1lesson35.py


"""
    Primes

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.

 

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 

Compare the results and performance of each of them.
"""


import math
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_prime in zip(numbers, results) if is_prime]


def filter_primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_prime in zip(numbers, results) if is_prime]


def main():
    # Measure ThreadPoolExecutor performance
    start_time = time.time()
    primes_threadpool = filter_primes_threadpool(NUMBERS)
    threadpool_time = time.time() - start_time

    # Measure ProcessPoolExecutor performance
    start_time = time.time()
    primes_processpool = filter_primes_processpool(NUMBERS)
    processpool_time = time.time() - start_time

    print("Primes using ThreadPoolExecutor:", primes_threadpool)
    print("Time taken by ThreadPoolExecutor:", threadpool_time)

    print("Primes using ProcessPoolExecutor:", primes_processpool)
    print("Time taken by ProcessPoolExecutor:", processpool_time)
    
    
if __name__ == "__main__":
    main()

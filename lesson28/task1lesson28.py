#task1lesson28.py


"""
A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list and 
the second pass moves "down." This alternating pattern continues until no more passes are necessary. 
Implement this variation and describe under what circumstances it might be appropriate.
"""


import random
import timeit 


def bubble_sort(array):
    m = len(array)
    for i in range(m):
        swapped = False
        for j in range(1, m-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                swapped = True
        if not swapped:
            break
    return array

def bubble_sort_reverse(array):
    n = len(array)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

        start += 1
            
    return array

        
if __name__ == '__main__':
    N = 20
    array = [random.randint(0, 100) for _ in range(N)]
    print(array)
    
    print(f"bubble_sort: {timeit.timeit('bubble_sort(array.copy())', globals=globals(), number=10000):.5}\n{bubble_sort(array.copy())}")
    print(f"bubble_sort_reverse: {timeit.timeit('bubble_sort_reverse(array.copy())', globals=globals(), number=10000):.5}\n{bubble_sort_reverse(array.copy())}")


"""
- **Переваги**:
  - Cocktail Shaker Sort може бути ефективнішим, ніж звичайне сортування бульбашкою, коли великі 
  елементи знаходяться на початку списку, а малі елементи - в кінці.
  - Зменшує кількість проходів, необхідних для сортування масиву, оскільки елементи переміщуються в 
  обох напрямках.

- **Обставини використання**:
  - Підходить для списків, де великі елементи знаходяться на початку, а малі - в кінці.
  - Може бути корисним для списків, які майже відсортовані, оскільки зменшує кількість необхідних 
  проходів.

"""
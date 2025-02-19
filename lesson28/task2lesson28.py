#task2lesson28.py


"""
    Implement the mergeSort function without using the slice operator.
"""


import random
import timeit 


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
            
    return array


def other_merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left_half = [array[i] for i in range(mid)]
        right_half = [array[i] for i in range(mid, len(array))]

        other_merge_sort(left_half)
        other_merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


if __name__ == '__main__':
    N = 20
    array = [random.randint(0, 100) for _ in range(N)]
    print(array)
    
    print(f"merge_sort: {timeit.timeit('merge_sort(array.copy())', globals=globals(), number=10000):.5}\n{merge_sort(array.copy())}")
    print(f"other_merge_sort: {timeit.timeit('other_merge_sort(array.copy())', globals=globals(), number=10000):.5}\n{other_merge_sort(array.copy())}")

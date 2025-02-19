#task3lesson28.py


"""
    One way to improve the quicksort is to use an insertion sort on lists that are small in 
    length (call it the "partition limit"). Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. 
    Perform analysis using different list sizes for the partition limit.
"""

import random
import timeit 


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)


def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp

    return right_mark


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def quicksort(array, low, high, partition_limit):
    if high - low <= partition_limit:  # Use insertion sort for small partitions
        insertion_sort(array, low, high)
    else:
        if low < high:
            pivot_index = quicksort_partition(array, low, high)
            quicksort(array, low, pivot_index - 1, partition_limit)  # Sort left partition
            quicksort(array, pivot_index + 1, high, partition_limit)  # Sort right partition
    return array

def quicksort_partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

if __name__ == '__main__':
    N = 100
    partition_limit = 10
    array = [random.randint(0, 100000) for _ in range(N)]
    print(array)
    
    print(f"quick_sort: {timeit.timeit('quick_sort(array.copy())', globals=globals(), number=10000):.5}\n{quick_sort(array.copy())}")
    print(f"quicksort witch partition_limit { partition_limit}: {timeit.timeit('quicksort(array.copy(), 0, len(array) - 1, partition_limit)', globals=globals(), number=10000):.5}\n{quicksort(array.copy(), 0, len(array) - 1, partition_limit)}")
    print(f"quicksort witch partition_limit { int(partition_limit*2)}: {timeit.timeit('quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*2))', globals=globals(), number=10000):.5}\n{quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*2))}")
    print(f"quicksort witch partition_limit { int(partition_limit*3)}: {timeit.timeit('quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*3))', globals=globals(), number=10000):.5}\n{quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*3))}")
    print(f"quicksort witch partition_limit { int(partition_limit*4)}: {timeit.timeit('quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*4))', globals=globals(), number=10000):.5}\n{quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*4))}")
    print(f"quicksort witch partition_limit { int(partition_limit*5)}: {timeit.timeit('quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*5))', globals=globals(), number=10000):.5}\n{quicksort(array.copy(), 0, len(array) - 1, int(partition_limit*5))}")
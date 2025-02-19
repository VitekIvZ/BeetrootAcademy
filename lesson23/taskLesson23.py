#taskLesson23.py


import time
import sys
sys.set_int_max_str_digits(0)

from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

#Match big O complexities with the code snippets below

# answers 
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n



def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n


def question3(first_list: List[int], second_list: List[int])-> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n

def test_func():

    print("question1:")
    start_time = time.time()
    assert question1([1, 2, 3], [2, 3, 4]) == [2, 3]
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question1([1, 2, 3], [4, 5, 6]) == []
    print(f"Execution time: {time.time() - start_time} seconds\n")

    print("question2:")
    start_time = time.time()
    assert question2(2) #== 1024
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question2(1) == 1
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question2(0) == 0
    print(f"Execution time: {time.time() - start_time} seconds\n")

    print("question3:")
    start_time = time.time()
    assert question3([1, 2, 3], [3, 4, 5]) == [1, 2, 3, [3, 4, 5], [3, 4, 5]]
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question3([1, 2, 3], [4, 5, 6]) == [1, 2, 3, [4, 5, 6], [4, 5, 6], [4, 5, 6]]
    print(f"Execution time: {time.time() - start_time} seconds\n")

    print("question4:")
    start_time = time.time()
    assert question4([1, 2, 3, 4, 5]) == 5
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question4([5, 4, 3, 2, 1]) == 5
    print(f"Execution time: {time.time() - start_time} seconds\n")

    print("question5:")
    start_time = time.time()
    assert question5(2) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question5(1) == [(0, 0)]
    print(f"Execution time: {time.time() - start_time} seconds\n")

    print("question6:")
    start_time = time.time()
    assert question6(8) == 1
    print(f"Execution time: {time.time() - start_time} seconds\n")
    start_time = time.time()
    assert question6(1) == 1
    print(f"Execution time: {time.time() - start_time} seconds\n")


if __name__ == '__main__':
    test_func()
    
from random import randint


# Лінійний алгоритм  O(n)
def line_search(element, container):  # container - common unsorted
    for elem in container:
        if elem == element:
            return True
    return False


# Бінарний пошук  O(log n)
def binary_search(element, container): 

    start_idx, end_idx = 0, len(container)-1
    idx = (start_idx + end_idx) // 2
    current = container[idx]
    condition = True
    counter = 0
    while current != element and condition:
        if element < current:
            end_idx = idx
        else:
            start_idx = idx
        idx = (start_idx + end_idx) // 2
        current = container[idx]
        condition = end_idx - start_idx != 1
        counter += 1
    print(f"{counter=}")   #  print(f"counter = {counter}")
    return current == element


if __name__ == '__main__':
    a, b = 1, 100
    N = 20
    con = [randint(a, b) for _ in range(N)]

    elem = 13
    print(f"{elem}: {line_search(elem, con)}")

    con.sort()
    print(con)

    elem = 13 # con[12]
    print(f"{elem}: {binary_search(elem, con)}")

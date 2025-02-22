import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":
    # Створення пулу процесів з 4 процесами
    with multiprocessing.Pool(processes=4) as pool:
        # Виконання завдань за допомогою методу map
        results = pool.map(square, range(10))
        print(results)
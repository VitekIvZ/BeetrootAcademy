class FibonacciSearch:
    def __init__(self, arr):
        self.arr = arr

    def fibonacci_search(self, x):
        n = len(self.arr)
        fib2 = 0  # (m-2)-е число Фібоначчі
        fib1 = 1  # (m-1)-е число Фібоначчі
        fibM = fib2 + fib1  # m-е число Фібоначчі

        # Знаходимо найменше число Фібоначчі, більше або рівне n
        while fibM < n:
            fib2 = fib1
            fib1 = fibM
            fibM = fib2 + fib1

        offset = -1  # Зсув для визначення діапазону пошуку

        while fibM > 1:
            i = min(offset + fib2, n - 1)  # Індекс для перевірки

            if self.arr[i] < x:
                # Зсуваємося вправо
                fibM = fib1
                fib1 = fib2
                fib2 = fibM - fib1
                offset = i
            elif self.arr[i] > x:
                # Зсуваємося вліво
                fibM = fib2
                fib1 = fib1 - fib2
                fib2 = fibM - fib1
            else:
                return i  # Елемент знайдено

        # Перевірка останнього елемента
        if fib1 and offset + 1 < n and self.arr[offset + 1] == x:
            return offset + 1

        return -1  # Елемент не знайдено


def main():
    arr = [2, 3, 4, 10, 40]
    x = 10

    search_instance = FibonacciSearch(arr)
    result = search_instance.fibonacci_search(x)

    print(f"Element is present at index {result}" if result != -1 else "Element is not present in array")


if __name__ == '__main__':
    main()
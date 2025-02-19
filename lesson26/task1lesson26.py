#task1lesson26.py
from binary_search import BinarySearch
from fibo_search import FibonacciSearch
import time

""""
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

Прочитати про Fibonacci search та імплементуйте його за допомогою Python. 
Визначте складність алгоритму та порівняйте його з бінарним пошуком
"""
def main():
    N = 100000000 # кількість елементів у списку
    my_list = [i for i in range(N)]
    
    x = 654321 # елемент, який шукаємо
    
    start_time = time.time()
    bSearch = BinarySearch(my_list)
    result = bSearch.binary_search_recursive(0, len(my_list)-1, x)
    print(f"Binary search: {result} --- {time.time() - start_time}")
    
    start_time = time.time()
    bSearch = FibonacciSearch(my_list)
    result = bSearch.fibonacci_search(x)
    print(f"Fibonacci search: {result} --- {time.time() - start_time}")
    
    

if __name__ == '__main__':
    main()
    

"""
### Складність алгоритмів

- **Бінарний пошук**:
  - Часова складність: O(log n)
  - Просторова складність: O(log n) (через рекурсію)

- **Fibonacci пошук**:
  - Часова складність: O(log n)
  - Просторова складність: O(1)

### Порівняння

- Обидва алгоритми мають однакову часову складність O(log n).
- Fibonacci пошук має перевагу в просторовій складності, оскільки використовує O(1) додаткової пам'яті, тоді як бінарний пошук використовує O(log n) через рекурсію.
- Fibonacci пошук може бути ефективнішим для великих масивів, де просторові обмеження є критичними.

"""
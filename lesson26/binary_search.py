class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def binary_search_recursive(self, low, high, x):
        if high >= low:
            mid = (high + low) // 2

            if self.arr[mid] == x:
                return mid
            elif self.arr[mid] > x:
                return self.binary_search_recursive(low, mid - 1, x)
            else:
                return self.binary_search_recursive(mid + 1, high, x)
        else:
            return -1

def main():
    arr = [2, 3, 4, 10, 40]
    x = 10

    search_instance = BinarySearch(arr)
    result = search_instance.binary_search_recursive(0, len(arr) - 1, x)

    print(f"Element is present at index {result}" if result != -1 else "Element is not present in array")
    
    
if __name__ == '__main__':
    main()

#task3lesson19.py


"""
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
        
def test():
    my_iterable = MyIterable([1, 2, 3, 4, 5])

    for item in my_iterable:
        print(item)  
        
    print(f"\n{my_iterable[0]}")  
    print(f"\n{my_iterable[4]}")  

    print(f"\n{my_iterable[5]}")       


if __name__ == "__main__":
    test()
    

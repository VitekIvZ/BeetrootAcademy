import sys

def fibon(n):
    res = []
    a = b = 1
    res.append(a)
    for _ in range(n-1):
        a, b = b, a + b
        res.append(a)
    return res

def fib_gen(n):
    a, b = 1, 1
    yield a
    for _ in range(n-1):
        a, b = b, a + b
        yield a


class FibIterator:
    def __init__(self, n):
        self.n = n
        self.index = 0
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration()
        if self.index == 0:
            self.index += 1
            return self.a
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return self.a
    
    
if __name__ == '__main__':
    n = 10
    
    print(fibon(n)) 
    
    for num in fib_gen(n):
        print(num, end=" ")
    print()
    

    fib_iter = FibIterator(n)
    for num in fib_iter:
        print(num, end=" ") 
    print()
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
            raise StopIteration
        if self.index == 0:
            self.index += 1
            return self.a
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return self.a


# iter(), next() => __iter__,  __next__
# 

def reverse_range(n, m):
    counter = n
    if m > n:
        raise Exception()
    while counter >= m:
        yield counter
        counter -= 1
    return "The end!!!"
 

class RevesedIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.curr = start + 1

    def __iter__(self):
        # self.curr = self.start
        return self
    
    def __next__(self):
        self.curr -= 1
        if self.curr >= self.stop:
            return self.curr 
        else:
            raise StopIteration()


if __name__ == '__main__':

    lst = [i for i in range(1, 11)]

    gen = (i for i in range(1, 11))

    it = iter(lst)

    # for elem in it:
    #     print(elem, end=' ')
    # print()

    # while True:
    #     try:
    #         elem = next(gen)
    #         print(elem, end=' ')
    #     except:
    #         break
    # print()

    # rev_it = RevesedIterator(5, 0)
    # for val in rev_it:
    #     print(val, end=' ')
    print(fibon(5))
    # print(sys.getsizeof(lst), sys.getsizeof(gen), sys.getsizeof(reversed(lst)))
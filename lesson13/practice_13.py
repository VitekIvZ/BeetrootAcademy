import time

CONST = 9845

glob_var = 34985.987

def counter():  # closure
    count = 0
    def inkrement():
        # global glob_var
        nonlocal count
        count += 1
        local_var = glob_var
        local_var /= 100
        return count
    return inkrement


def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n-1)


def timer(func, *args, **kwargs):
    # print("Do something before")
    # print(dir(func))
    # print(dir(func.__code__))
    start = time.time()
    result = func(*args, **kwargs)
    # print("Do something after")
    print(f"func {func.__name__} run  {time.time()-start}")
    return result


if __name__ == '__main__':
    # print("global var = ", glob_var)
    x = counter()
    # y = counter()
    # print(x(), x(), y(), x(), y(), y())
    # print(x())
    var_1, var_2 = 12, 15
    # maggic_func = eval(f"lambda var_{1}, var_{2}: var_{1} * var_{2}")
    # print(maggic_func(var_1, var_2))
    # print(timer(factor, 10)) 
    # print(globals())
    # print("global var = ", glob_var)

    sqr = lambda x: x*x   #  sqr(4)
    lst = [i for i in range(10)]
    lst_sqr = [sqr(elem) for elem in lst]

    # def map_sqr(sqr, lst):
    #     return [sqr(elem) for elem in lst]
    
    # print(sum(map(sqr, range(10))))  #map() - 

    N = 12
    matrix = [ [i * j for j in range(N)]  for i in range(N)]
    # print(matrix)
    for row in matrix:
        # print(' '.join(map(str, row)))
        print(''.join(map("{:^5}".format, row)))

    print('\n'.join(map(  lambda row: ''.join(map("{:^5}".format, row)     ), matrix)) )




#  3*n^2 - 5 n + 3 < 3*n^2 + |5*n| + 3 < 3*n^2 + 5*n^2 + 3*n^2 < 11 * n^2 = O(n^2)

# 1. O(1)  
# 2. O(n) 
# 3. O(log n)
# 4. O(n*log n)
# 5. O(n^2)
# 6. O(n^3)
# 7. O(2^n)
# 8. O(n!)

# O(1)  
a = 10
n = 100
lst = [i for i in range(n)]
lst[25], lst.append(100), lst.pop()      #  100 => 150  mojo 
dct = {str(i): i for i in lst}
dct['1'], '50' in dct  # set()  O(1)
lst.insert(0, -1), lst.pop(0), 50 in lst     # O(n)

# O(n)
# for elem in lst:
#     z = elem*elem
#     print(z)

# for i in range(len(lst)):
#     elem = lst[i]
#     z = elem*elem
#     # z = lst[i]*lst[i]
#     print(z)

# O(log n)

# 100 => ?  50 < 25 < 13 < 6 < 3 < 1 > 2

i = n
while i > 0:
    sqr = i*i
    i //= 2

# O(n^2)

lst_2 = [[i*j for j in range(n)] for i in range(n)]


lst_II = []   # 4 
for i in range(n):
    for j in range(n):
        lst_II.append(i*j)


# O(n^3)   A[n x k] * B[k x m]  = C[n x m]
matrixA = [
    [2, 4, 7],
    [3, 6, 9],
    [1, 4, 6],
]

matrixB = [
    [2, 4, 7],
    [3, 6, 9],
    [1, 4, 6],
]

matrixC = [
    [0, 0, 0],     # 2*2+4*3+7*1, 
    [0, 0, 0],
    [0, 0, 0],
]

for i in range(3):
    for j in range(3):
        for k in range(3):
            matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

print(matrixC)   # n => n^3  k*n => k^3*n^3


# O(2^n)

def fibon(n):
    if n <= 1:
        return n
    else:
        return fibon(n-1)+fibon(n-2)
    
fibon(5) # 15  
fibon(10) # 55
fibon(20) # 6765

# O(n!)

# permutation
from itertools import  permutations


# Write a Python program to create 
# a generator that generates all possible permutations of a string.
# abc  (3! = 1 * 2 * 3 = 6): abc, acb, bac, bca, cab, cba
# print  (5! = 1 * 2 * 3 * 4 * 5 = 120)
def str_permut(text):
    if len(text) == 1:
        yield text
    else:
        for idx, char in enumerate(text):
            # print(char)
            remaining = text[:idx] + text[idx+1:]
            for permut in str_permut(remaining):
                yield char + permut

print(len(list(str_permut('abc'))))
print(len(list(str_permut('print'))))

print(list(permutations('ABC', 3)))
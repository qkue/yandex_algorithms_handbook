# Python 3.12.1

def fib(a):
    if n <= 1:
        return n
    f_0, f_1 = 0, 1
    for i in range(2, a+1):
        f_0, f_1 = f_1, f_0 + f_1
    return f_1

n = int(input())
print(fib(n))

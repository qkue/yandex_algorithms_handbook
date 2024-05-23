# Python 3.12.1

def fib(a):
    if a <= 1:
        return a
    f_0, f_1 = 0, 1
    for i in range(1, a):
        f_0, f_1 = f_1, (f_0 + f_1) % 10
    return f_1


n = int(input())
print(fib(n))

# Python 3.12.1

def move(n, start, finish):
    if n == 1:
        print(start, finish)
    else:
        tmp = 6 - start - finish
        move(n - 1, start, tmp)
        print(start, finish)
        move(n - 1, tmp, finish)

def t(T):
    if T == 1:
        return 1
    else:
        return 2 * t(T - 1) + 1

n = int(input())
print(t(n))

move(n, 1, 3)

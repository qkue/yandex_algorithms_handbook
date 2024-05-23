# Python 3.12.1

def pisano(modulo):
    cache = [0, 1]
    cur, _next, period = 0, 1, 0
    while True:
        cur, _next = _next, (cur + _next) % modulo
        cache.append(_next)
        period += 1
        if cur == 0 and _next == 1:
            return cache, period


def fib(a, b):
    if a <= 1:
        return a

    table, b_pisano = pisano(b)
    res = table[a % b_pisano]
    return (res if res > 0 else 10) - 1

n = int(input())
print(fib(n+2, 10))

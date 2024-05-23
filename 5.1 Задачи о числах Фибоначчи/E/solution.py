# Python 3.12.1

def pisano(modulo):
    cache = [0, 1]
    cur, _next, period = 0, 1, 0
    cur_100, _next100 = 0, 1
    while True:
        cur, _next = _next, (cur + _next) % modulo
        cur_100, _next100 = _next100, (cur_100 + _next100) % 100
        cache.append(_next100)
        period += 1
        if cur == 0 and _next == 1:
            return cache, period


def fib(a, b):
    if a <= 1:
        return (a if a == 0 else a - 1)

    table, b_pisano = pisano(b)
    res = table[a % b_pisano]
    return (res if res > 0 else 10) - 1

m, n = map(int, input().split())
print((fib(n+2, 10) - fib(m+1, 10)) % 10)

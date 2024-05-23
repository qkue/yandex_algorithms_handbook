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
    return table[a % b_pisano]
    # f_0, f_1 = 0, 1
    # for i in range(1, (a % b_pisano)):
    #     f_0, f_1 = f_1, (f_0 + f_1) % m
    #    # print(f_1)
    # return f_1

n, m = map(int, input().split())
print(fib(n, m))

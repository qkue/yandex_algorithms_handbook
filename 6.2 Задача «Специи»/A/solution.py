# Python 3.12.1

n, w = map(int, input().split())

spicy = [tuple(map(float, input().split())) for _ in range(n)]
spicy.sort(key = lambda x: x[0] / x[1])
cost = 0

while w > 0 and spicy:
    loop_spicy_c, loop_spicy_w = spicy.pop()
    loop_amount = min(loop_spicy_w, w)
    value = (loop_spicy_c / loop_spicy_w) * loop_amount
    w -= loop_amount
    cost += value
print(cost)

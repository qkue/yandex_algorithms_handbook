# Python 3.12.1
# Решение до банального простое, гораздо больше времени ушло на понимание условия задачи. Пример задачи с подвохом.

n, k, w = map(int, input().split())
order = sorted([list(map(int, input().split())) for _ in range(k)], key = lambda x: -x[0])

result = 0

place = n * w
for i in order:
    if place:
        c, p = i
        amount = min(p, place)
        result += c * amount
        place -= amount
print(result)

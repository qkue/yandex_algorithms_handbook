# Python 3.12.1

n, el = map(int, input().split())
xi = sorted(list(map(int, input().split())))

count = 0
r_point = None

for x in xi:
    if r_point is None or x > r_point:
        count += 1
        r_point = x + el
print(count)

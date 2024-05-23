# Python 3.12.1

n = int(input())
lr = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: x[1])

count = 0
points = []

for point in lr:
    left, right = point
    if not points or left > points[-1]:
        points.append(right)
        count += 1
print(count)
print(*points)

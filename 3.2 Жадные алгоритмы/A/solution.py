# Python 3.12.1

line = []
res = []

for lin in range(int(input())):
    line.append(tuple(map(int, input().split())))

line_sorted = sorted(line, key = lambda x: x[::-1])
while line_sorted:
    left, right = line_sorted.pop(0)
    res.append((left, right))
    for lin in line_sorted[::-1]:
        if lin[0] <= right:
            line_sorted.remove(lin)

print(len(res))

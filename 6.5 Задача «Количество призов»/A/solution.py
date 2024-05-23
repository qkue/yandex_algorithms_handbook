# Python 3.12.1

n = int(input())

res = 0
for i in range(int(max(1, n ** 0.5 - 2)), n):
    x = (i * (i +1)) / 2
    if x > n:
        break
    res = i
print(res)

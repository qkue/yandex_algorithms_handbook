# Python 3.12.1

n = int(input())
p = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    result += p[i] * c[i]
print(result)

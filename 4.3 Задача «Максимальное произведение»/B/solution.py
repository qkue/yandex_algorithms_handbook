# Python 3.12.1

n = int(input())

if 1 + ((n - 2) * 2) > (1.5 * n):
    print('Yes')
    print(n, end=' ')
    print(*range(1, n))
else:
    print('No')

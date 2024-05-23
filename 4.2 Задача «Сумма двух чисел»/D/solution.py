# Python 3.12.1

n, m = map(int, input().split())
matrix_f = [list(map(int, input().split())) for k in range(n)]
matrix_s = [list(map(int, input().split())) for k in range(n)]

res = [[matrix_f[j][i] + matrix_s[j][i] for i in range(m)] for j in range(n)]

for x in range(n):
    for y in range(m):
        print(res[x][y], end=' ')

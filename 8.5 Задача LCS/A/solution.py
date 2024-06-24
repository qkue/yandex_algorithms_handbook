# Python 3.12.3

n = int(input())
first_data = list(map(int, input().split()))
m = int(input())
second_data = list(map(int, input().split()))

table = [[0] * (m + 1) for _ in range(n + 1)]
#print(*table, sep = '\n')

for row in range(1, n + 1):
    for col in range(1, m + 1):
        # table[row][col] = table[row - 1][col]
        table[row][col] = max(table[row - 1][col], table[row][col - 1])
        if first_data[row - 1] == second_data[col - 1]:
            table[row][col] = max(table[row][col], table[row - 1][col - 1] + 1)

print(table[row][col])

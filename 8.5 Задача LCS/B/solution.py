# Python 3.12.3
# Рекурсивный алгоритм с мемо(р)изацией выглядел бы более читаемо, но упирался в 12 тесте в Time Limit

from sys import stdin

n = int(stdin.readline().rstrip())
first_data = list(map(int, stdin.readline().split()))
m = int(stdin.readline().rstrip())
second_data = list(map(int, stdin.readline().split()))
b = int(stdin.readline().rstrip())
third_data = list(map(int, stdin.readline().split()))

dp = [[[0] * (b + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for row in range(1, n + 1):
    for seg in range(1, m + 1):
        for elem in range(1, b + 1):
            dp[row][seg][elem] = max(dp[row - 1][seg][elem], dp[row][seg - 1][elem], dp[row][seg][elem - 1])
            if first_data[row - 1] == second_data[seg - 1] and second_data[seg - 1] == third_data[elem - 1]:
                dp[row][seg][elem] = max(dp[row][seg][elem], dp[row - 1][seg - 1][elem - 1] + 1)

print(dp[row][seg][elem])


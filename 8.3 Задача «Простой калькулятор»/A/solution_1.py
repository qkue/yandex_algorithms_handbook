# Python 3.12.3

n = int(input())
dp = [0] * (n + 1)

for num in range(2, n + 1):
    dp[num] = 1 + dp[num - 1]
    if not (num % 2):
        dp[num] = min(dp[num], dp[num // 2] + 1)
    if not (num % 3):
        dp[num] = min(dp[num], dp[num // 3] + 1)
#print(*dp)

operations = list()
num = n
while num > 1:
    operations.append(num)
    if dp[num] == dp[num - 1] + 1:
        num -= 1
    elif not (num % 2) and dp[num] == dp[num // 2] + 1:
        num //= 2
    elif not (num % 3) and dp[num] == dp[num // 3] + 1:
        num //= 3
operations.append(num)

operations.reverse()
print(dp[n])
print(*operations)

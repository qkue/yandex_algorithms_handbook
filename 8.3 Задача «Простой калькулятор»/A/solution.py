# Python 3.12.1

n = int(input())

dp = [0] * (n + 1)
prev = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 2 == 0 and (dp[i // 2] + 1 < dp[i]):
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    if i % 3 == 0 and (dp[i // 3] + 1 < dp[i]):
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

answer = []
ans_ind = n
while ans_ind > 0:
    answer.append(ans_ind)
    ans_ind = prev[ans_ind]
answer.reverse()

print(dp[n])
print(*answer)

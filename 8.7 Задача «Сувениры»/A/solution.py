# Python 3.12.3

from sys import stdin

n = int(stdin.readline().rstrip())
gold = [0] + list(map(int, stdin.readline().split()))

def pirate(arr, n):    
    sum_arr = sum(arr)
    if (sum_arr % 3):
        return False
    V = sum_arr // 3
    dp = [[[False] * (V + 1) for _ in range(V + 1)] for _ in range(n + 1)]
    # print(*dp, sep = '\n')
    dp[0][0][0] = True

    for i in range(1, n + 1):
        for s1 in range(V + 1):
            for s2 in range(V + 1):
                dp[i][s1][s2] = dp[i - 1][s1][s2]
                if s1 >= arr[i]:
                    dp[i][s1][s2] = dp[i][s1][s2] or dp[i - 1][s1 - arr[i]][s2]
                if s2 >= arr[i]:
                    dp[i][s1][s2] = dp[i][s1][s2] or dp[i - 1][s1][s2 - arr[i]]
    return dp[n][V][V]
                    
print(1 if pirate(gold, n) == True else 0)

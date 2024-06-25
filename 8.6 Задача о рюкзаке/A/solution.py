# Python 3.12.3

from sys import stdin

w, n = map(int, stdin.readline().split())
gold = list(map(int, stdin.readline().split()))

def knapsack(arr, weight, n):    
    dp = [[False] * (n + 1) for _ in range(weight + 1)]
    # print(*dp, sep = '\n')
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(weight + 1):
            if arr[i-1] > w:
                dp[w][i] = dp[w][i - 1]
            else:
                dp[w][i] = (dp[w][i - 1] or dp[w - arr[i - 1]][i - 1])
    # print('ready dp')
    # print(*dp, sep = '\n')
    
    for w in range(weight, -1, -1):
        #for i in range(n, -1, -1):
        if dp[w][n] == True:
            return w
    return 0
print(knapsack(gold, w, n))


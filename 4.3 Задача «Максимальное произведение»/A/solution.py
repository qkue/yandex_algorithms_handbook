# Python 3.12.1

def MaxPairwiseProductBySorting(a):
    a.sort()
    return a[-1]*a[-2]

n = int(input())
m = list(map(int, input().split()))

print(MaxPairwiseProductBySorting(m))

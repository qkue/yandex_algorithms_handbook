# Python 3.12.1

def max_pair(arr):
    arr.sort()
    right = arr[-2] * arr[-1] * arr[-3]
    left = arr[0] * arr[1] * arr[-1]
    print(max(right, left))

n = int(input())
m = list(map(int, input().split()))
max_pair(m)

# Python 3.12.1

def max_pair(arr):
    arr.sort()
    right = arr[-2] * arr[-1] * arr[-3] * arr[-4]
    left = arr[0] * arr[1] * arr[-1] * arr[-2]
    full_left = arr[0] * arr[1] * arr[2] * arr[3]
    print(max(right, left, full_left))

n = int(input())
m = list(map(int, input().split()))
max_pair(m)

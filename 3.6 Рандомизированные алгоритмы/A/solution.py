# Python 3.12.1

def lomuto(n, arr):
    pivot = arr[0]
    i = 1
    for j in range(1, n):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[0], arr[i - 1] = arr[i - 1], arr[0]
    return arr

n = int(input())
a = list(map(int, input().split()))
result = lomuto(n, a)
print(' '.join(map(str, result)))

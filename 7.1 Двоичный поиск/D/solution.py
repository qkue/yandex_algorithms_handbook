# Python 3.12.1

n, k = map(int, input().split())
x = sorted(set(map(int, input().split())))

def right_len(point, key, lenght):
    end = point[0] + lenght
    key -= 1
    for p in point:
        if end < p:
            key -= 1
            end = p + lenght
            if key < 0: 
                return False
    return True

def min_len(n, arr, k):
    if k >= len(arr):
        return 0
    minimum = 0
    maximum = arr[len(arr)-1] - arr[0]
    while minimum != maximum:
        mid = minimum + (maximum - minimum) // 2
        if mid == maximum or mid == minimum:
            return maximum
        if right_len(arr, k, mid):
            maximum = mid
        else:
            minimum = mid 

    return maximum

print(min_len(n, x, k))

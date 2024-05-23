# Python 3.12.1

def bin_search(n, arr, q):
    min_index = 0
    max_index = n - 1
    while max_index >= min_index:
        middle_ind = (min_index + max_index) // 2
        if arr[middle_ind] == q:
            return middle_ind
        elif arr[middle_ind] < q:
            min_index = middle_ind + 1
        else:
            max_index = middle_ind - 1
    return -1

n = int(input())
k = list(map(int, input().split()))
q = int(input())

print(bin_search(n, k, q))

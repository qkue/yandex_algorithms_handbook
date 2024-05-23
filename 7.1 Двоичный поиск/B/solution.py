# Python 3.12.1

def many_bin_search(n, arr, m, arr_to_search):
    result = []
    for i in (arr_to_search):
        min_index = 0
        max_index = n - 1
        ans = -1
        while max_index >= min_index:
            middle_ind = (min_index + max_index) // 2
            if arr[middle_ind] == i:
                ans = middle_ind
                break
            elif arr[middle_ind] > i:
                max_index = middle_ind - 1
            else:
                min_index = middle_ind + 1
        result.append(ans)
    return result        

n = int(input())
k = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

for x in many_bin_search(n, k, m, q):
    print(x)

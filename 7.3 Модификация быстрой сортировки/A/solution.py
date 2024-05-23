# Python 3.12.1

n = int(input())
a = list(map(int, input().split()))

def randomqs(len_a, arr):
    import random

    if len_a <= 1:
        return arr
    random_element = random.choice(arr)
    arr_small = [num for num in arr if num < random_element]
    arr_equal = [num for num in arr if num == random_element]
    arr_big = [num for num in arr if num > random_element]
    sort_arr_small = randomqs(len(arr_small), arr_small)
    sort_arr_big = randomqs(len(arr_big), arr_big)
    final = sort_arr_small + arr_equal + sort_arr_big
    return final

print(*randomqs(n, a))

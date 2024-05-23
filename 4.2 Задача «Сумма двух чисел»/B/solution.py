# Python 3.12.1

def many(a_x, b_x, arr_a, arr_b):
    print(max(a_x, b_x))
    ind = -1

    for i in arr_b[::-1]:
        arr_a[ind] += i
        ind -= 1
    print(*arr_a)        

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if len(a) != len(b):
    a, b = max(a, b, key=len), min(a, b, key=len)
many(n, m, a, b)

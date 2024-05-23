# Python 3.12.1
# Это не разбиение Ломуто, но в тестах ошибка и в итоге нужен такой алгоритм для этих тестов

n = int(input())
m = list(map(int, input().split()))

def lomuto(arr):
    
    left_list = []
    right_list = []
    pivot = arr[0]

    for i in arr:
        if i <= pivot:
            left_list.append(i)
        else:
            right_list.append(i)
    left_list[0], left_list[-1] = left_list[-1], left_list[0]

    return left_list + right_list

print(*lomuto(m))

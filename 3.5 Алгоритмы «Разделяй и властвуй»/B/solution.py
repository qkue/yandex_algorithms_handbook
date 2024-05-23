# Python 3.12.1
# В условии сказано "Задано n отсортированных по неубыванию последовательностей..." но это не так. После таких случаев, начинаешь везде перестраховываться :-)

def merge(list_1, list_2):
    sorted_list = []
    left_ind = 0
    right_ind = 0

    while left_ind <= len(list_1)-1 and right_ind <= len(list_2)-1 and list_1 and list_2:
        if list_1[left_ind] <= list_2[right_ind]:
            sorted_list.append(list_1[left_ind])
            left_ind += 1
        elif list_2[right_ind] <= list_1[left_ind]:
            sorted_list.append(list_2[right_ind])
            right_ind += 1

    if left_ind-1 == len(list_1) - 1 or not list_1:
        sorted_list.extend(list_2[right_ind:])
    elif right_ind-1 == len(list_2) - 1 or not list_2:
        sorted_list.extend(list_1[left_ind:])
    return sorted_list

n = int(input())
res = []

for _ in range(n):
    t = input()
    input_list = list(map(int, input().split()))
    input_list.sort()
    res = merge(res, input_list)
    

print(*res)

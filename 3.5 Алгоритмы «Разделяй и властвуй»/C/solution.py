# Python 3.12.1

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

def merge_sort(list_full):
    if len(list_full) == 1:
        return list_full
    lenght = len(list_full) // 2
    first_half = list_full[:lenght]
    second_half = list_full[lenght:]
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)
    sort_list = merge(sorted_first_half, sorted_second_half)
    return sort_list

n = int(input())
res = list(map(int, input().split()))

print(*merge_sort(res))

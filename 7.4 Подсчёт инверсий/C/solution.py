# Python 3.12.1

n = int(input())
list_a = list(map(int, input().split()))

def Merge(left_half, right_half):
    sorted_list = []
    inversions = 0
    #left.reverse()
    #right.reverse()
    while left_half and right_half:
        #left_elem = left.pop()
        #r_elem = right.pop()
        if left_half[0] < right_half[0]:
            sorted_list.append(left_half.pop(0))
        else:
            sorted_list.append(right_half.pop(0))
            inversions += len(left_half)
    sorted_list += left_half if left_half else right_half
    return sorted_list, inversions



def count_inversion(n, a):
    if n <= 1:
        return (a, 0)
    pivot = n // 2
    left_half = a[: pivot]
    right_half = a[pivot:]
    left_half, left_rec = count_inversion(pivot, left_half)
    right_half, right_rec = count_inversion(n-pivot, right_half)
    a, inversion = Merge(left_half, right_half)
    return (a, (left_rec + right_rec + inversion))

print(count_inversion(n, list_a)[1])

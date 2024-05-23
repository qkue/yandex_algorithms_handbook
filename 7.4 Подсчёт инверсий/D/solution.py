# Python 3.12.1
# Одно из сложнейших решений. Почти неделя на поиск решения для питона которое вошло в лимиты.

from collections import deque

n = int(input())

# sorting
if n < 3:
    print(0)
else:
    p = [[k, int(v)] for k, v in enumerate(input().split(), 0)]
    def quicksort(arr, left, right):
        
        if right <= left:
            return 0
        pivot = arr[right][1]
        
        i_space = left
        j_space = right - 1
        while i_space <= j_space:
            while arr[i_space][1] < pivot:
                i_space += 1
            while arr[j_space][1] > pivot:
                j_space -= 1
            if i_space >= j_space:
                break
            arr[i_space], arr[j_space] = arr[j_space], arr[i_space]

        arr[i_space], arr[right] = arr[right], arr[i_space]
        
        j_space = i_space - 1
        i_space += 1

        quicksort(arr, left, j_space)
        quicksort(arr, i_space, right)
        

    def Merge(left_half, right_half, len_left, len_right):

        sorted_list = []
        inversions = 0
        left = 0
        right = 0

        while left < len_left and right < len_right:
            le = left_half[left]
            ri = right_half[right]
            if le <= ri:
                sorted_list.append(le)
                left += 1
            else:
                sorted_list.append(ri)
                right += 1
                inversions += len_left - left
        while left < len_left:
            sorted_list.append(left_half[left])
            left += 1
        while right < len_right:
            sorted_list.append(right_half[right])
            right += 1        
        return sorted_list, inversions

   
    def count_inversion(b, a):
        if b <= 1:
            return (a, 0)
        
        pivot = b // 2
        left_half = a[:pivot]
        right_half = a[pivot:]
        left_half, left_rec = count_inversion(pivot, left_half)
        right_half, right_rec = count_inversion(b-pivot, right_half)
        a, inversion = Merge(left_half, right_half, pivot, b-pivot)
        sum_invers = (left_rec + right_rec + inversion)
        return (a, sum_invers)
      
    p.sort(key=lambda x: x[1])
    sorted_seq = [ind[0] for ind in p]

    result = count_inversion(n, sorted_seq)[1]
    testing_row = deque(sorted_seq)
    answer = result

    for _ in range(n-1):
        testing_row.rotate(-1)
        last_elem = testing_row[-1]

        result = result - int(last_elem) + ((n-1) - int(last_elem))

        if result < answer:
            answer = result

    print(answer)

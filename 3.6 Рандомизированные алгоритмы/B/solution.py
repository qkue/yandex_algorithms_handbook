# Python 3.12.1

from random import choice

def lomuto(arr, low, high):
    random_n = choice(range(low, high+1))
    arr[random_n], arr[high] = arr[high], arr[random_n]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        piv = lomuto(arr, low, high)
        quick_sort(arr, low, piv - 1) 
        quick_sort(arr, piv + 1, high) 

n = int(input())
m = list(map(int, input().split()))
quick_sort(m, 0, n-1)
print(*m)

'''
QuickSort(c):
     if |c| = 1: // только один элемент
        return c
     m = c[1] // возьмем первый элемент c
     // определим элементы c_small меньше m
     // определим элементы c_large больше m
     QuickSort(c_small)
     QuickSort(c_large)
     // объединим c_small, m и c_large в сортированный список c_sorted
     return c_sorted
'''

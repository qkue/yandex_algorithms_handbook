# Python 3.12.1

def select_sort(seq):
    for i in range(len(seq) - 1):
        min_index = i
        for k in range(i + 1, len(seq)):
            if seq[k] < seq[min_index]:
                min_index = k
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq

n = int(input())
a = list(map(int, input().split()))

print(*select_sort(a))

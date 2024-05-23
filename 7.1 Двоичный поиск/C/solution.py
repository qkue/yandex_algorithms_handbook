# Python 3.12.1

def bin_search(n_k, arr_k, m_q, arr_q):
    final = []
    for number_q in arr_q:
        min_index = 0
        max_index = n_k - 1
        result = 0
        min_index_seq = -1
        while max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if arr_k[mid_index] == number_q:
                max_index = mid_index - 1
                min_index_seq = mid_index
            elif arr_k[mid_index] > number_q:
                max_index = mid_index - 1
            else: 
                min_index = mid_index + 1
        min_index = min_index_seq
        max_index = n_k - 1
        max_index_seq = min_index_seq
        while min_index_seq != -1 and max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if arr_k[mid_index] == number_q:
                min_index = mid_index + 1
                max_index_seq = mid_index
            elif arr_k[mid_index] > number_q:
                max_index = mid_index - 1
            else: 
                min_index = mid_index + 1
        
        # while min_index_seq <= n_k - 1 and arr_k[min_index_seq] == number_q:
        #     result += 1
        #     min_index_seq += 1
        if min_index_seq == -1:
            final.append(0)
        else:
            final.append(max_index_seq - min_index_seq + 1)
    return final    

n = int(input())
k = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

print(*bin_search(n, k, m, q))

# Python 3.12.1

n = int(input())
ax = list(map(int, input().split()))

def maxi_el(num, arr):
    if num < 4:
        ret_dic = {}
        for elem in arr:
            ret_dic[elem] = ret_dic.get(elem, 0) + 1
        return ret_dic

    mid = num // 4
    left_arr = arr[:num // 4]
    right_arr = arr[num // 4:]
    rec_left = maxi_el(len(left_arr), left_arr)
    rec_right = maxi_el(len(right_arr), right_arr)
    final_dict = dict()
    for key in (set(rec_left) | set(rec_right)):
        
        if arr.count(key) > num // 4:
            final_dict[key] = 1

    
    return final_dict

print((1 if len(maxi_el(n, ax)) == 3 else 0))

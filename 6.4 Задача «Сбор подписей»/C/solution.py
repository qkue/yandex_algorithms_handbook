# Python 3.12.1

n, el = map(int, input().split())
xi = sorted(list(map(int, input().split())))

if len(set(xi)) <= el:
    print(0)
else:
    sub_point = [(xi[p+1] - xi[p], p+1) for p in range(len(xi)-1)]
    sub_point.sort(key = lambda x: -x[0])
    ind_to_list = sorted(sub_point[:el-1], key = lambda y: -y[1])
    result = 0
    for ind in ind_to_list:
        cnt, i = ind
        result += xi[i:][-1] - xi[i:][0]
        del xi[i:]
    result += xi[-1] - xi[0]
    print(result)

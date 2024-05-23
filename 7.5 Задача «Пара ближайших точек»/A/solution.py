# Python 3.12.1
# Задача, которой особенно горжусь, потратил почти 3 дня и нашёл решение проходящее лимиты на питоне.

def _closest_pair(points, min_dist, left, right):
    if right - left <= 3:
        #print(f'points - {points[left:right]}')
        brute_dist = min([((points[i][0] -  points[j][0]) ** 2 + (points[i][1] -  points[j][1]) ** 2) ** 0.5 for i in range(left, right - 1) for j in range(i + 1, right)])

        if min_dist > brute_dist:
            min_dist = brute_dist
        return 

    m = (left + right) // 2


    _closest_pair(points, min_dist, left, m)
    _closest_pair(points, min_dist, m, right)

    #return min(left_pair, right_pair)

def final(points, min_dist):
    _closest_pair(points, min_dist, 0, len(points))

    close_y = [p for p in sorted(points, key = lambda f: f[1]) if abs(p[0] - points[len(points) // 2][0]) < min_dist]
    
    for i in range(len(close_y) - 1):

        for j in range(i + 1, min(i + 8, len(close_y))):

            if close_y[j][1] - close_y[i][1]> min_dist:
                break    
            min_dist = min(min_dist, ((close_y[i][0] -  close_y[j][0]) ** 2 + (close_y[i][1] -  close_y[j][1]) ** 2) ** 0.5)
    return min_dist


from sys import stdin
n = int(stdin.readline().strip())
points = sorted(tuple(map(int, stdin.readline().strip().split())) for i in range(n))
min_dist = 10**9
#t_buffer = []
print(round(final(points, min_dist), 6))


# Python 3.12.3

n, m = map(int, input().split())
maximum = n * m
labirinth = [[-1] * (m) for _ in range(n)]
"""
-2 = стена (#)
-1 = пустая клетка (.)
0 = старт (S)
"""
start, finish = None, None
for row in range(n):
    blocks = input()
    for col in range(m):
        block = blocks[col]
        if block == '#':
            block = -2
        elif block == '.':
            block = -1
        elif block == 'S':
            start = (row, col)
            block = 0
        elif block == 'F':
            finish = (row, col)
            block = -1
        labirinth[row][col] = block
# print(*labirinth, sep = '\n')

destination = [[maximum] * (m) for _ in range(n)] # расстояние
destination[start[0]][start[1]] = 0
prev = [[maximum] * (m) for _ in range(n)] 
prev[start[0]][start[1]] = -1
# для восстановления ответа храним кортеж (предыдущая точка, направление)

from collections import deque
queue = deque()
queue.append(start)
dir_row = [0, -1, 0, 1]
dir_col = [-1, 0, 1, 0]
dir_sign = ['L', 'U', 'R', 'D']
while queue:
    row, col = queue.popleft()
    for shift in range(len(dir_row)):
        now_row = row + dir_row[shift]
        now_col = col + dir_col[shift]
        if labirinth[now_row][now_col] == - 1:
            labirinth[now_row][now_col] = labirinth[row][col] + 1
            prev[now_row][now_col] = (row, col, dir_sign[shift])
            queue.append((now_row, now_col))
# print(*labirinth, sep = '\n')
# print('NEXT TABLE IS PREV')
# print(*prev, sep = '\n')
steps = labirinth[finish[0]][finish[1]]
print(steps)
if steps > 0:
    back_track = []
    move = prev[finish[0]][finish[1]]
    while move != -1:
        # print(move)
        back_track.append(move[2])
        move = prev[move[0]][move[1]]
    back_track.reverse()
print(''.join(back_track))


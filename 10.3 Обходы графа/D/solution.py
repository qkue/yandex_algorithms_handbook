# Python 3.12.3
# Мне понравилось, как они плавно нас подводят к сложной задаче, это пока ещё лёгкая :-)

from collections import deque

def BFS(labirinth, prev, start_point, access_granted, mark):
    queue = deque()
    queue.append(start_point)
    dir_row = [0, -1, 0, 1]
    dir_col = [-1, 0, 1, 0]
    dir_sign = ['L', 'U', 'R', 'D']
    while queue:
        row, col = queue.popleft()
        for shift in range(len(dir_row)):
            now_row = row + dir_row[shift]
            now_col = col + dir_col[shift]
            if labirinth[now_row][now_col][0] in access_granted:
                labirinth[now_row][now_col] = (mark, labirinth[row][col][1] + 1)
                prev[now_row][now_col] = (row, col, dir_sign[shift])
                queue.append((now_row, now_col))

def recovery_track(prev, start_point, end_point):
    back_track = []
    move = prev[start_point[0]][start_point[1]]
    prev[end_point[0]][end_point[1]] = -1
    while move != -1:
        back_track.append(move[2])
        move = prev[move[0]][move[1]]
    back_track.reverse()
    return (''.join(back_track))

n, m = map(int, input().split())
maximum = n * m
labirinth = [[(-1, 0)] * (m) for _ in range(n)]
"""
-2 = стена (#)
-1 = пустая клетка (.)
-11 = это будет метка пустой клетки для второго прохода, что в первом проходе мы прошли по ней
0 = старт (S)
"""
special = dict()
for row in range(n):
    blocks = input()
    for col in range(m):
        block = blocks[col]
        if block == '#':
            block = -2
        elif block == '.':
            block = -1
        else:
            special[block] = (row, col)
            if block == 'S':
                block = 0
            elif block == 'D':
                block = -2
            else: # F and K
                block = -1           
        labirinth[row][col] = (block, 0)
prev = [[maximum] * (m) for _ in range(n)] 
prev[special['S'][0]][special['S'][1]] = -1
# для восстановления ответа храним кортеж (предыдущая точка, направление)
avaliable_moves = [-1]
BFS(labirinth, prev, special['S'], avaliable_moves, -11)
finish_row, finish_col  = special['F']
key_row, key_col = special['K']
if labirinth[finish_row][finish_col][0] == -11:
    path = recovery_track(prev, special['F'], special['S'])
    print(labirinth[finish_row][finish_col][1])
    print(path)
elif labirinth[key_row][key_col][0] == -11:
    first_half_path = recovery_track(prev, special['K'], special['S']) + 'P'
    first_half_steps = labirinth[key_row][key_col][1] + 1
    door_row, door_col = special['D']
    labirinth[door_row][door_col] = (-1, 0) # делаем дверь доступной для открытия
    avaliable_moves.append(-11)
    avaliable_moves.append(0)
    BFS(labirinth, prev, special['K'], avaliable_moves, -111)
    if labirinth[finish_row][finish_col][0] == -111:
        second_half_path = recovery_track(prev, special['F'], special['K'])
        full_path = first_half_path + second_half_path
        second_half_steps = labirinth[finish_row][finish_col][1]
        full_steps = first_half_steps + second_half_steps
        print(second_half_steps + 1, full_path, sep='\n')
    else:
        print(-1)
else:
    print(-1)

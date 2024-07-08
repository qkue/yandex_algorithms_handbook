# Python 3.12.3
# Эта задача заняла моё время, потому что сначала не уделил должного времени планированию. Не делайте так.
# Сперва пошёл по пути рекурсивного алгоритма, но ожидаемо, он тяжелее итеративного и его гораздо сложнее уложить в лимиты.
# Пришлось отказаться от рекурсии и сделать такой алгоритм. Да, он получился немного большим :)
# Мне задача понравилась, жаль, что такая задача появляется только к концу хэндбука.

from sys import stdin
n, m = map(int, stdin.readline().split())
maximum = n * m * 2
labirinth = [[0] * (m) for _ in range(n)] 
# (проверка на доступный ход на текущем уровне, количество ходов, тип клетки)

"""
-1 = стена (#)
-2 = дверь (D)
-3 = ключ (K)
-4 = финиш (F)
-5 = пустая клетка (.)
каждое значение меньше -5 на единицу при каждом проходе это будет метка пустой клетки
0 = старт (S)
"""
special = dict()
for row in range(n):
    blocks = stdin.readline().rstrip()
    for col in range(m):
        block = blocks[col]
        if block == '#':
            block = -1
        elif block == '.':
            block = -5
        else:
            special[block] = (row, col)
            special[(row, col)] = block
            block = -5
            # if block == 'S':
            #     block = -5
            # elif block in door_char:
            #     block = -5
            # elif block in 'abcdeghijk':
            #     block = -5
            # elif block == 'F':
            #     block = -5
            
        labirinth[row][col] = (block, 0, blocks[col])

key_char = []
door_char = []
door_key = dict()
k = int(stdin.readline().rstrip())
for _ in range(k):
    k, v = stdin.readline().split()
    door_char.append(k)
    key_char.append(v)
    door_key[k] = v
obtained_keys = set()
key_char = ''.join(key_char)
door_char = ''.join(door_char)
# print(f'create labirinth')
# print(*labirinth, sep = '\n')

answer = (35000, 'inf')
visited = [set() for _ in range(20)]
queue = [0] * (maximum)
start_row, start_col = special['S']
start_point = (start_row, start_col, 0, 1, 'S') # row, col, steps, level, path
queue_front = 0
queue_back = 0
queue[queue_back] = start_point
queue_back = (queue_back + 1) % maximum
visited[1].add((start_row, start_col, 1,'S'))
dir_row = [0, -1, 0, 1]
dir_col = [-1, 0, 1, 0]
while queue_back != queue_front:
    ROW, COL, STEPS, LEVEL, PATH = queue[queue_front]
    queue_front = (queue_front + 1) % maximum
    if STEPS + len(PATH) > answer[0]:
        continue
    for shift in range(4):
            now_row = ROW + dir_row[shift]
            now_col = COL + dir_col[shift]

            if (now_row, now_col, LEVEL, PATH) not in visited[LEVEL]:
                # print(f'now_row = {now_row}, now_col = {now_col}, steps = {STEPS}, level = {LEVEL}, path = {PATH}')
                number, _, type_block = labirinth[now_row][now_col]
                if type_block in key_char:
                    # print(f'key = {type_block}')
                    if type_block not in PATH:
                        queue[queue_back] = (now_row, now_col, STEPS + 1, LEVEL + 1, PATH + type_block)
                        queue_back = (queue_back + 1) % maximum
                        visited[LEVEL].add((now_row, now_col, LEVEL + 1, PATH + type_block))

                    queue[queue_back] = (now_row, now_col, STEPS + 1, LEVEL, PATH)
                    visited[LEVEL].add((now_row, now_col, LEVEL, PATH))
                    queue_back = (queue_back + 1) % maximum
                    
                elif type_block in door_char:
                    door = special[(now_row, now_col)]
                    if door_key[door] in PATH:
                        queue[queue_back] = (now_row, now_col, STEPS + 1, LEVEL, PATH)    
                        queue_back = (queue_back + 1) % maximum
                        visited[LEVEL].add((now_row, now_col, LEVEL, PATH))
                elif type_block == 'F':
                    queue[queue_back] = (now_row, now_col, STEPS + 1, LEVEL, PATH)
                    queue_back = (queue_back + 1) % maximum
                    visited[LEVEL].add((now_row, now_col, LEVEL, PATH))
                    result = STEPS + len(PATH)
                    if answer[0] > result:
                        answer = ((result, PATH))
                    # print(f' result = {(now_row, now_col, STEPS + 1, LEVEL, PATH)}')
                elif number == -5:
                    queue[queue_back] = (now_row, now_col, STEPS + 1, LEVEL, PATH)
                    queue_back = (queue_back + 1) % maximum
                    visited[LEVEL].add((now_row, now_col, LEVEL, PATH))
            # print(queue)


def BFS(labirinth, prev, start_point, access_granted, mark, founded_key, special, queue):
    # queue = [0] * (maximum)
    queue_front = 0
    queue_back = 0
    queue[queue_back] = start_point
    queue_back = (queue_back + 1) % maximum
    dir_row = [0, -1, 0, 1]
    dir_col = [-1, 0, 1, 0]
    dir_sign = ['L', 'U', 'R', 'D']
    
    while queue_back != queue_front:
        row, col = queue[queue_front]
        queue_front = (queue_front + 1) % maximum
        for shift in range(len(dir_row)):
            now_row = row + dir_row[shift]
            now_col = col + dir_col[shift]
                        
            if labirinth[now_row][now_col][2] in door_char and labirinth[now_row][now_col][0] in access_granted:
                door = special[(now_row, now_col)]
                if door_key[door] in founded_key:
                    labirinth[now_row][now_col] = (mark, labirinth[row][col][1] + 1, labirinth[now_row][now_col][2])
                    prev[now_row][now_col] = (row, col, dir_sign[shift])
                    queue[queue_back] = (now_row, now_col)
                    queue_back = (queue_back + 1) % maximum
            elif labirinth[now_row][now_col][0] in access_granted:
                labirinth[now_row][now_col] = (mark, labirinth[row][col][1] + 1, labirinth[now_row][now_col][2])
                prev[now_row][now_col] = (row, col, dir_sign[shift])
                queue[queue_back] = (now_row, now_col)
                queue_back = (queue_back + 1) % maximum

def recovery_track(prev, start_point, end_point):
    back_track = []
    move = prev[start_point[0]][start_point[1]]
    save_pos = prev[end_point[0]][end_point[1]]
    prev[end_point[0]][end_point[1]] = -1
    # print(f'prev in recovery track')
    # print(*prev, sep = '\n')
    while move != -1:
        back_track.append(move[2])
        move = prev[move[0]][move[1]]
    prev[end_point[0]][end_point[1]] = save_pos
    back_track.reverse()
    return back_track 

# answer = min(result, key = lambda p: p[0])
# print(answer)
# if min_value_path[1] == 'inf':
if special['S'] == special['F']:
    print(0)
    print(fdc)
elif answer[1] == 'inf':
    print(-1)
else:
    # path = min_value_path[1]
    path = answer[1]
    if path[-1] != 'F':
        path += 'F'
    full_path = []
    founded_key = set()
    prev = [[maximum] * (m) for _ in range(n)] 
    # prev[special['S'][0]][special['S'][1]] = -1
    avaliable_moves = set()
    last_mark = labirinth[special['S'][0]][special['S'][1]][0]
    avaliable_moves.add(last_mark)
    flag_num = last_mark
    for key in range(len(path) - 1):
        if path[key] in key_char:
            founded_key.add(path[key])
        avaliable_moves.add(flag_num)
        flag_num -= 1
        BFS(labirinth, prev, special[path[key]], avaliable_moves, flag_num, founded_key, special, queue)
        piece_track = recovery_track(prev, special[path[key + 1]], special[path[key]])
        if path[key + 1] in key_char:
            piece_track.append('P')
        full_path.extend(piece_track)


    print(len(full_path))
    print(''.join(full_path))

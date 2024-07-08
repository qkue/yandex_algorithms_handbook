# Python 3.12.3
# Оказалось, что не только предыдущая интересная :)
# Рекомендую постараться ещё немного победить эту задачку, вы получите наслаждение от решения.

from sys import stdin
data = stdin.read().split()
# with open('\input.txt', 'rt', encoding = 'utf-8') as file_input:
#     data = file_input.read().split()
ind = 0
output_answer = []
test = []
k_max = 5
t = (int(data[ind]))
ind += 1
for _ in range(t):
    n = int(data[ind])
    m = int(data[ind + 1])
    k = int(data[ind + 2])
    s = int(data[ind + 3])
    ind += 4
    desktop = []
    for i in range(n):
        desktop.append(data[ind])
        ind += 1
    test.append((n, m, k, s, desktop))
# print(test)

for n, m, k, s, desktop in test:
    # already_touch = set()
    program_place_on_desktop = [[] for _ in range(k_max + 1)]
    for row in range(n):
        for col in range(m):
            current_block = desktop[row][col]
            if current_block.isdigit():
                program_place_on_desktop[int(current_block)].append((row, col))
    # print(f'program_place_on_desktop = {program_place_on_desktop}')

    window = [[] for _ in range(k + 1)]
    for program in range(1, k + 1):
        programm_row, programm_col = program_place_on_desktop[program][0]
        for row in range(s):
            for col in range(s):
                check_row = programm_row - row
                check_col = programm_col - col 
                if 0 <= check_row and 0 <= check_col:
                    check_left_point = all([((check_row <= x <= check_row + (s - 1)) and (check_col <= y <= check_col + (s - 1))) for x, y in program_place_on_desktop[program]])
                    if check_left_point:
                        # temp = [(check_row + i, check_col + j) for j in range(s) for i in range(s)]
                        # print(f'temp = {temp}')
                        temp = []
                        isBreak = False
                        for i in range(s):
                            if isBreak:
                                break
                            for j in range(s):
                                point_row_square = check_row + i
                                point_col_square = check_col + j
                                # print(f'point_row = {point_row_square}, point_col = {point_col_square}')
                                if point_row_square >= n or point_col_square >= m or desktop[point_row_square][point_col_square] == '.':
                                    temp = []
                                    isBreak = True
                                    break
                                temp.append((point_row_square, point_col_square))
                        if temp:
                            window[program].append(temp)
    # print(f'window = {window}')

    this_result = 0
    # used = set()
    stack = ['0']
    # for i in range(1, k + 1):
    #     lists_of_points_start = window[i]
    #     for left_top in lists_of_points_start:
    #         stack.append(str(i))
        # stack.append(str(i)) # элемент, путь
        # used.add(str(i))
        # print(f'stack = {stack}')
    while stack:
        path = stack.pop()
        if len(path) > k:
            # print(f'path = {path}')
            this_result += 1
        else:
            for number in range(1, k + 1):
                if str(number) not in path:
                # if path + str(number) not in used and str(number) not in path:
                    for option in window[number]:
                        suitable_cond = all([(desktop[row][col] == str(number) or (desktop[row][col] not in path)) for row, col in option])
                        if suitable_cond:
                            stack.append(path + str(number))
                            # used.add(path + str(number))
    output_answer.append(this_result)
    # print(f' this result = {this_result}')
if any([i == 0 for i in output_answer]):
    print(fdfsdf)
else:
    print('\n'.join(str(i) for i in output_answer))



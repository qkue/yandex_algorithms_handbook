# Python 3.12.3
# Не стал чистить и делать код красивым, хочу сохранить этого монстра на память. Обернул код самым тяжелым тестом и пробовал разные варианты, подходы, оптимизации.
# В итоге, единственная оптимизация, которая пройдёт на питоне это максимально сокращать количество проходов. На плюсах, возможно, получилось бы более простое решение уложить в такой огромный лимит

from sys import stdin
data = stdin.read().split()
# with open('C:\python\python_alghoritm_handbook\input.txt', 'rt', encoding = 'utf-8') as file_input:
#     data = file_input.read().split()
ind = 0
output_answer = []
test = []
k_max = 9
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
            if current_block != '.':
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
                    check_left_point = True
                    for x, y in program_place_on_desktop[program]:
                        if not ((check_row <= x <= check_row + (s - 1)) and (check_col <= y <= check_col + (s - 1))):
                            check_left_point = False
                            break
                    # check_left_point = all([((check_row <= x <= check_row + (s - 1)) and (check_col <= y <= check_col + (s - 1))) for x, y in program_place_on_desktop[program]])
                    if check_left_point:
                        # temp = [(check_row + i, check_col + j) for j in range(s) for i in range(s)]
                        # print(f'temp = {temp}')
                        # temp = []
                        temp = set()
                        isBreak = False
                        for i in range(s):
                            if isBreak:
                                break
                            for j in range(s):
                                point_row_square = check_row + i
                                point_col_square = check_col + j
                                # print(f'point_row = {point_row_square}, point_col = {point_col_square}')

                                if point_row_square >= n or point_col_square >= m or desktop[point_row_square][point_col_square] == '.':
                                    temp = set()
                                    isBreak = True
                                    break
                                temp.add(desktop[point_row_square][point_col_square])
                                # temp.append((point_row_square, point_col_square))
                        if temp:
                            window[program].append(temp)
    # print(f'window = {window}')
    this_result = 0
    # used = set()
    maximum = (n * m) + 10000
    queue = [0] * maximum
    queue_front = 0
    queue_back = 0
    # stack = ['0']
    # stack = [0]
    # stack = []
    # str_range = {str(i) for i in range(1, k + 1)}
    remaining_nums_dict = dict()
    # remaining_nums_dict['123456789'] = [{'0'}, 0, ''.join(str(i) for i in range(1, k + 1))]
    
    dict_num_set = {'1': {'1'}, '2': {'2'}, '3': {'3'}, '4': {'4'}, '5': {'5'}, '6': {'6'}, '7': {'7'}, '8': {'8'}, '9': {'9'}}
    # dict_left_nums = {'1': '23456789', '2': '13456789', '3': '12456789', '4': '12356789', '5': '12346789', '6': '12345789', '7': '12345689', '8': '12345679', '9': '12345678'}
    # queue[queue_back] = '123456789'
    # queue_back = (queue_back + 1) % maximum
    for digit in range(1, k + 1):
        str_digit = set(str(digit))
        # stack.append((dict_num_set[str(digit)], len(window[digit]), str_range.difference(dict_num_set[str(digit)])))
        # queue[queue_back] = ((dict_num_set[str(digit)], len(window[digit]), str_range.difference(dict_num_set[str(digit)])))
        # queue_back = (queue_back + 1) % maximum
        num = ''.join(str(i) for i in range(1, k + 1) if i != digit)
        remaining_nums_dict[num] = [dict_num_set[str(digit)], len(window[digit]), num]
        # remaining_nums_dict[dict_left_nums[str(digit)]] = [dict_num_set[str(digit)], len(window[digit]), dict_left_nums[str(digit)]]
        queue[queue_back] = num
        # queue[queue_back] = dict_left_nums[str(digit)]
        queue_back = (queue_back + 1) % maximum
    # print(f'remaining_nums_dict = {remaining_nums_dict}')
    # print(stack)
    # nums = {i for i in range(1, k + 1)}
    # maximum = (n * m) ** 3
    # num_for_check_result = 10 ** (k - 1)
    # queue = [0] * maximum
    # queue_front = 0
    # queue_back = 0
    # queue[queue_back] = ['0']
    # queue[queue_back] = '0'
    # queue[queue_back] = ('0', nums) 
    # queue[queue_back] = 0
    # queue_back = (queue_back + 1) % maximum
    # num_range = range(1, k + 1)
    # while stack:
    while queue_back != queue_front:
        # path, mul, numbers = stack.pop()
        # print(f' path = {path}, mul = {mul}')
        # path = queue[queue_front]
        # path, numbers = queue[queue_front]
        # print(f'path = {path}')
        path, mul, numbers = remaining_nums_dict[queue[queue_front]]
        queue_front = (queue_front + 1) % maximum
        if len(path) >= k:
        # if len(path) > k:
        # if path - num_for_check_result > 0:
            # print(f'path = {path}')
            this_result += mul
        else:
            # for number in range(1, k + 1):
            # for number in numbers:
            for number in numbers:
                # print(numbers)
                # if str(number) not in str(path):
                # if str(number) not in path:
                # if path + str(number) not in used and str(number) not in path:
                    common_path = ''
                    common_mul = 0
                    for option in window[int(number)]:
                        # suitable_cond = True
                        # for row, col in option:
                        # for pixel in option:
                        if not option.intersection(path):
                            # pixel = desktop[row][col]
                            # if pixel in path or pixel == '.':
                            # if pixel in path:
                            #     suitable_cond = False
                            #     break
                        # suitable_cond = all([(desktop[row][col] == str(number) or (desktop[row][col] not in path and desktop[row][col] != '.')) for row, col in option])
                            # if suitable_cond:
                            if not common_path:
                                common_path = path.union(dict_num_set[number])
                            common_mul += mul
                            # common_mul += len(window[int(number)])
                            # queue[queue_back] = (path + [str(number)])
                            # queue[queue_back] = (path + str(number))
                            # queue[queue_back] = (path + str(number), numbers.difference({number}))
                            # queue[queue_back] = (path * 10 + number)
                            # queue_back = (queue_back + 1) % maximum
                            # set_number = {number}
                            # stack.append((path.union(dict_num_set[number]), mul, numbers.difference(dict_num_set[number])))
                            # stack.append(path * 10 + number)
                            # used.add(path + str(number))
                    if common_path:
                        now_numbers = numbers.replace(number, '', 1)
                        if now_numbers not in remaining_nums_dict:
                            remaining_nums_dict[now_numbers] = [common_path, common_mul, now_numbers]
                            queue[queue_back] = now_numbers
                            queue_back = (queue_back + 1) % maximum
                        else:
                            remaining_nums_dict[now_numbers][1] += common_mul
                        # print(f'after operation remaining nums dict = {remaining_nums_dict}')
                        
                        # queue[queue_back] = ((common_path, common_mul, numbers.difference(dict_num_set[number])))
                        
                            
    output_answer.append(this_result)
    # print(f' this result = {this_result}')

print('\n'.join(str(i) for i in output_answer))

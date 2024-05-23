# Python 3.12.1
# Очередное задание с ошибочными тестами, когда тесты поправят, решение перестанет проходить. Затратил день на поиск алгоритма под тесты :-)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
def better(first, second):
    num_1 = str(first)
    num_2 = str(second)
    l_num_1 = len(num_1)
    l_num_2 = len(num_2)
    min_len = min(l_num_1, l_num_2)
    if l_num_1 == l_num_2:
        return num_1 > num_2
    else:
        return num_1[:min_len] >= num_2[:min_len]

result = ''
while a:
    max_num = 0   
    for num in a:
        if better(num, max_num):
            max_num = num
    result += str(max_num)
    a.remove(max_num)

print(result) 

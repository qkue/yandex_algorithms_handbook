# Python 3.12.3

x, y = map(int, input().split())
minimum = min(x, y)
maximum = max(x, y) + 40 #нужен небольшой запас, есть тесты которые проверяют, что оптимальнее получить значение больше и сделать вычитание

from collections import deque # можно было бы использовать очередь в виде кольцевого буфера, но и этого хватило
queue = deque()
used = [0] * (maximum + 1)
queue.append(x)
destination = [maximum] * (maximum + 1)
destination[x] = 0
used[x] = 1
isMinusUsed = False
while queue:
    vertex = queue.popleft()
    for i in range(1, 10): # с - цифра, задание немного с хитринкой :-)
        plus = vertex + i
        minus = vertex - i
        mul = vertex * i
        options = [minus, plus, mul] # можно поиграться с оптимизацией, если описать случаи когда нужно совершать различные операции
        if not isMinusUsed: # обязательно нужно проверять и с 0, возможно так будет быстрее дойти
            isMinusUsed = True
            options.append(0)
        for var in options:
            if 0 <= var <= maximum  and not used[var]:
                queue.append(var)
                used[var] = 1
                destination[var] = destination[vertex] + 1
print(destination[y])


# Python 3.12.3

from sys import stdin
from collections import deque 
# Мне не захотелось писать класс односторонней очереди, взял готовую
# двухстороннюю из стандартной библиотеки, она тоже прекрасно подойдет
# В тестах нет отрицательных чисел, этот код только для положительных чисел и 0.

text = stdin.readline().rstrip()
postfix_expression = []
queue = deque()

storage = 0
isNumber = False
for sym in text:
    if sym.isdigit():
        storage = storage * 10 + int(sym)
        isNumber = True
    else:
        if isNumber:
            postfix_expression.append(storage)
            isNumber = False
            storage = 0
        
        if sym == '*' and queue and queue[0] == '*':
            while queue[0] != '*':
                postfix_expression.append(queue.popleft())
        elif sym == '+' or sym == '-':
            while queue and queue[0] != '(':
                postfix_expression.append(queue.popleft())   
        elif sym == ')':
            while queue[0] != '(':
                postfix_expression.append(queue.popleft())
            queue.popleft()
            continue
        queue.appendleft(sym)
if isNumber:           
    postfix_expression.append(storage)
while queue:
    postfix_expression.append(queue.popleft())
#print(postfix_expression)
for operand in postfix_expression:
    if isinstance(operand, int):
        queue.appendleft(operand)
    else:
        num_2 = queue.popleft()
        num_1 = queue.popleft()
        queue.appendleft(eval(f'{num_1}{operand}{num_2}'))

answer = 0
if queue:
    answer = queue.popleft()
print(answer)

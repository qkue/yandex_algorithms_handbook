# Python 3.12.1
# дек на двух стеках реализован в последней задаче подглавы СТЕК

from collections import deque

deq = deque()
n = int(input())
answer = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        deq.append(query[1])
    elif query[0] == '2':
        deq.popleft()

    t = '-1'
    if len(deq):
        t = deq[0]
    answer.append(t)

print('\n'.join(answer))

# Python 3.12.3
# Задачка-отдых

from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

component = []

used = set()
for begin in range(1, n + 1):
    if begin not in used:
        now_chain = []
        stack = []
        stack.append(begin)
        used.add(begin)
        now_chain.append(begin)
        while stack:
            start_point = stack.pop()
            for his_friend in graph[start_point]:
                if his_friend not in used:
                    used.add(his_friend)
                    now_chain.append(his_friend)
                    stack.append(his_friend)
        component.append(now_chain)
if len(component) > 1:
    answer = []
    for island in range(1, len(component)):
        answer.append(f'{component[island - 1][-1]} {component[island][-1]}')
    print(len(answer))
    print('\n'.join(answer))
else:
    print(0)


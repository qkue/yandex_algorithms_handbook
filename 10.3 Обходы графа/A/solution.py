# Python 3.12.3

from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
nums = []
for _ in range(m):
    v1, v2, t = map(int, stdin.readline().split())
    if (t == 2):
        v1, v2 = v2, v1
    graph[v1].append(v2)
result = [False] * (n + 1)

def DFS(graph, vertex, color, result, records, isCicle):
    color[vertex] = 1
    records[vertex] = 0
    # result[vertex] += 1
    # print(f'in DFS vertex = {vertex}')
    games = [0]
    for to in graph[vertex]:
        # print(f'to = {to} graph = {graph[vertex]}')
        if color[to] == 1 and to != vertex:
            isCicle[0] = True
            return 0
        if not color[to]:
            games.append(DFS(graph, to, color, result, records, isCicle))
        else:
            games.append(records[to])
        
        if isCicle[0] == True:
            return 0
    records[vertex] = max(games) + 1
    # print(f'res = {records[vertex]}\n records = {records}')
    result[records[vertex]] = True
    color[vertex] = 2
    return records[vertex]

color = [0] * (n + 1)
"""
0 = не посещенная
1 - зашли (серая)
2 - вышли (черная)
"""
# used = [False for _ in range(n + 1)]
isCicle = [False]
records = [0] * (n + 1)
for v in range(1, n + 1):
    if not color[v]:
        # print(f'start v = {v}')
        DFS(graph, v, color, result, records, isCicle)
# print('wrong =', result)

isRight = True

for res in range(1, n + 1):
    if result[res] != True:
        isRight = False
        break

print("YES" if (isRight and not isCicle[0]) or n == 1 else "NO")

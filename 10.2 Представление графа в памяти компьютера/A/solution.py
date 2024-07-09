# Python 3.12.3

from sys import stdin

n, m = map(int, stdin.readline().split())
first_graph = [[0] * (n + 1) for _ in range(n + 1)] 
second_graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    row = list(map(int, stdin.readline().split()[1:]))
    if len(row) > 1:
        for stop in range(1, len(row)):
            now_stop = row[stop]
            prev_stop = row[stop - 1]
            first_graph[now_stop][prev_stop] = 1
            first_graph[prev_stop][now_stop] = 1

        for bus_stop_from in range(len(row)):
            for bus_stop_to in range(len(row)):
                if bus_stop_from != bus_stop_to:
                    second_graph[row[bus_stop_from]][row[bus_stop_to]] = 1

for i in range(1, len(first_graph)):
    print(' '.join(str(first_graph[i][j]) for j in range(1, len(first_graph[i]))))
for i in range(1, len(second_graph)):
    print(' '.join(str(second_graph[i][j]) for j in range(1, len(second_graph[i]))))


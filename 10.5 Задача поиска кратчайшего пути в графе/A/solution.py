# Python 3.12.3
# Прошло почти два дня, прежде чем придумал как сделать решение оптимальным для условий. Самые тяжелые тесты начинаются с 29 теста.
# Хорошая задачка, перечитал про алгоритм Дейкстры много информации, посмотрел разные реализации.
# Плохо, когда для всех языков одни ограничения, т.к. на С++ не нужно делать столько оптимизаций для решения этой задачи. В то время когда, для
# не такого быстрого Пайтона, придётся хорошенько подумать на алгоритмом. Но возможно, уже в какой-нибудь 3.15 или 3.20 версии будет залетать что-то попроще :-)
# Задумался, а как Пайтонисты протаскивали это решение на какой-нибудь версии Пайтона 3.5 или 3.6 они были ещё не такие быстрые. Т.е. тут есть ещё какие-то возможные улучшения

def restore_path(recovery_path, end_point, path, from_memo = False, isReverse = True):
    if not from_memo:
        point = end_point
        now_path = []
        while (point != -1):
            now_path.append(point)
            point = path[point]
        for point in range(len(now_path) - 2, -1, -1):
            recovery_path.append(now_path[point])
        return now_path
    else:
        if isReverse:
            for point in range(len(path) - 2, -1, -1):
                recovery_path.append(path[point])
        else:
            for point in range(1, len(path)):
                recovery_path.append(path[point])

def dijkstra(graph, now_best_distance, recovery_path, start, end, n, m):
    result_graph = [inf] * (n + 1)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    result_graph[start] = 0
    path = [-1] * (n + 1)
    while priority_queue:
        weight, vertex = heapq.heappop(priority_queue)
        if weight > result_graph[vertex]:
            continue

        if vertex == end:
            break
        if result_graph[vertex] > now_best_distance:
            return inf
        for edge in graph[vertex]:
            edge_num, edge_w = edge 
            if result_graph[vertex] + edge_w < result_graph[edge_num]:
                result_graph[edge_num] = result_graph[vertex] + edge_w
                path[edge_num] = vertex
                heapq.heappush(priority_queue, (result_graph[edge_num], edge_num))
    path = restore_path(recovery_path, vertex, path)
    return (result_graph[end], path)

def total_path_distance(graph, memo, now_best_distance, important_points, n, m):
    total_distance = 0
    full_path = [important_points[0]]
    for i in range(len(important_points) - 1):
        start = important_points[i]
        end = important_points[i + 1]
        if (start, end) in memo:
            dist, path, memo_access, switcher = memo[(start, end)]
            total_distance += dist
            if total_distance > now_best_distance:
                break
            restore_path(full_path, start, path, memo_access, switcher)
            continue
        distances, input_path = dijkstra(graph, now_best_distance, full_path, start, end, n, m)
        memo[(start, end)] = (distances, input_path, True, True)
        memo[(end, start)] = (distances, input_path, True, False)
        total_distance += distances
        if total_distance > now_best_distance:
            break
    return (total_distance, full_path)

def find_optimal_path_(graph, memo, required_points, warehouse, n, m):
    best_distance = inf
    best_path = []
    for permutation in permutations(required_points):
        permutation = (warehouse, permutation[0], permutation[1], permutation[2], warehouse)
        current_distance, current_path = total_path_distance(graph, memo, best_distance, permutation, n, m)
        if current_distance < best_distance:
            best_distance = current_distance
            best_path = current_path
    return best_distance, best_path

from itertools import permutations
from sys import stdin
import heapq

n, m, V, point_1, point_2, point_3 = map(int, stdin.readline().split())
inf = 10 ** 10
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, weight = map(int, stdin.readline().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))
required_points = [point_1, point_2, point_3]
memo = dict()
best_distance, best_path = find_optimal_path_(graph, memo, required_points, V, n, m)
print(len(best_path))
print(' '.join(str(i) for i in best_path))


"""
# TEST

5 7 3 2 4 5
2 3 2
3 4 1
4 2 3
5 4 4 
5 3 50
1 5 1
2 1 1

"""

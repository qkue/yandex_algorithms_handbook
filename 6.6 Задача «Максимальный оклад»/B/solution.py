# Python 3.12.1
# Да, в этой главе 2 задачи с плохими тестами. В очередной раз пришлось искать алгоритм для тестов, а не условий задачи. Времени ушло примерно полдня

n, k = map(int, input().split())
a = list(map(int, input().split()))
my_robot = a[k-1]
a.sort()
weak = len(a[:a.index(my_robot)])
strong = len(a[a.index(my_robot) + 1:])

result = 0
while weak:
    if strong % 2:
        weak -= 1
    weak //= 2
    strong //= 2
    result += 1
print(result)

# Python 3.12.1

   
class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def size(self):
        return True if self.array else False
    
    def back(self):
        if self.size():
            return self.array[-1]
        else:
            return False

arr = Stack()
n = int(input())
queries = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    while arr.size() and queries[i] > arr.back()[0]:
        elem, num = arr.pop()
        answer[i] += answer[num] + 1

    arr.push((queries[i], i))

print(*answer)

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
            return -1

arr = Stack()
n = int(input())
answer = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        arr.push(query[1])
    elif query[0] == '2':
        arr.pop()
        
    answer.append(str(arr.back()))

print('\n'.join(answer))

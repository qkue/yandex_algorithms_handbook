# Python 3.12.1
# материал, который помогает понять идею https://codeforces.com/blog/entry/71687?locale=ru


   
class Stack:
    def __init__(self, length):
        self.array = []
        #self.array = [0] * length
        #self.cnt = 0

    def push(self, item):
        # self.array[self.cnt] = item
        # self.cnt += 1
        self.array.append(item)

    def pop(self):
        # self.cnt -= 1
        # item = self.array[self.cnt]
        
        # return item
        return self.array.pop()

    def size(self):
        return True if self.array else False
    
    def back(self):
        if self.size():
            return self.array[-1]
        else:
            return False

from sys import stdin

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
queries = list(map(int, stdin.readline().split()))

arr = Stack(n)
temp_arr = Stack(k)
inf = 3 * 10 ** 5 + 1

answer = 0
temp_min = inf

for i in range(k):
    temp_arr.push(queries[i])
    if temp_min > queries[i]:
        temp_min = queries[i]
answer += temp_min
temp_min = inf

for i in range(k, n):

    if not arr.size():
        cur_min = inf
        while temp_arr.size():
            if cur_min > temp_arr.back():
                cur_min = temp_arr.back()
            arr.push(cur_min)
            temp_arr.pop()
        temp_min = inf
    arr.pop()

    temp_arr.push(queries[i])
    if temp_min > queries[i]:
        temp_min = queries[i]

    res = temp_min
    if arr.size():
        res = min(res, arr.back())
    answer += res
    
print(answer)

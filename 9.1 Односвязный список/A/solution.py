# Python 3.12.1

class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0

    def see_len(self):
        return self.lenght

    def give_index(self, index):
        current = self.head
        while index>1:
            current = current.next
            index -= 1
        return current.value

    def add(self, value): # вставка в начало
        self.head = LinkedNode(value, self.head)
        self.lenght += 1

    def insert(self, index, value): # вставка на позицию index
        if self.head is None or index == 0:
            self.add(value)

        else:
            current = self.head
            while current.next is not None and index > 1:
                current = current.next
                index -= 1
            current.next = LinkedNode(value, current.next)
        self.lenght += 1
    
    def remove(self, index=1):
        if index == 1 or self.head.next is None:
            self.head = self.head.next

        else:
            current = self.head
            while current.next.next is not None and index > 2:
                current = current.next
                index -= 1
            current.next = current.next.next
        self.lenght -= 1

    

class LinkedNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next
    
link = LinkedList()

answer = []
n = int(input())
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1], query[2]
        link.insert(x, y)
    elif query[0] == 2:
        answer.append(str(link.give_index(query[1])))
    elif query[0] == 3:
        link.remove(query[1])

print('\n'.join(answer))

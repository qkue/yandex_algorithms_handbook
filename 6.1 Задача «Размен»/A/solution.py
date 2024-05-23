# Python 3.12.1

final = []
cnt = 0
n = int(input())

for ten in range((n // 10) + 1):
        
    for five in range(((n - (10 * ten)) // 5) + 1):
        one = n - 10 * ten - 5 * five
        steps = str(ten + five + one)        
        final.append((steps + ' ' + '10 ' * ten + '5 ' * five + '1 ' * one).rstrip())
        cnt += 1
print(cnt)
print(*final, sep='\n')

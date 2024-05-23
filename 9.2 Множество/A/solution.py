# Python 3.12.1

numbers = set()

n = int(input())
answer = []

for _ in range(n):
    q, num = input().split()
    if q == '1':
        numbers.add(num)
    elif q == '2':
        if num in numbers:
            answer.append('1')
        else:
            answer.append('0')
            
print('\n'.join(answer))

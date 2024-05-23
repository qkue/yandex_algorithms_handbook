# Python 3.12.1

unknown_dict = dict()
answer = []

q = int(input())
for _ in range(q):
    query = input().split()
    if query[0] == '1':
        unknown_dict[query[1]] = query[2]
    elif query[0] == '2':
        temp = unknown_dict.get(query[1], '-1')
        answer.append(temp)

print('\n'.join(answer))

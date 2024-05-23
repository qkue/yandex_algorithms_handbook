# Python 3.12.1


n, s = map(int, input().split())

things = [int(input()) for _ in range(n)]
things.sort(reverse=True)
count = 0

while things:
    if things[-1] <= s:
        s -= things.pop()
        count += 1
    else:
        things.pop()
print(count)

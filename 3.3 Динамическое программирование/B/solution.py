# Python 3.12.1

n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
rocks = dict()
rocks[(0,0)] = 'Loose'

if n == m or (((n - m) % 3) == 0):
    print('Loose')
else:
    print('Win')

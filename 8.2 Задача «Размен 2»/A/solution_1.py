# Python 3.12.1

import sys
sys. setrecursionlimit(1500)

table = dict()

def change(money):
    if money not in table:
        if money == 0:
            table[money] = 0
        else:
            result = 10 ** 3
            for c in [1, 3, 4]:
                if c <= money:
                    result = min(result, 1 + change(money - c))
                table[money] = result
    return table[money]
m = int(input())
print(change(m))

# Python 3.12.1

import math

xx, yy = map(int, input().split())

print(int(math.factorial(xx + yy - 1) / (math.factorial(yy) * (math.factorial(xx - 1)))))

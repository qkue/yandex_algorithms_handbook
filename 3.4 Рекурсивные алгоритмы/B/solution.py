# Python 3.12.1

def big_t(m):
    k = m - round((2 * m + 1) ** 0.5) + 1
    
    if m == 1:
        return 1
    else:
        return 2 * big_t(k) + t(m - k)

def t(T):
    if T == 1:
        return 1
    else:
        return 2 * t(T - 1) + 1

n = int(input())
print(big_t(n))

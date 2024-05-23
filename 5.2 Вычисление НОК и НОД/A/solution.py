# Python 3.12.1

def GCD(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a,b)


n, m = map(int, input().split())
print(GCD(n, m))

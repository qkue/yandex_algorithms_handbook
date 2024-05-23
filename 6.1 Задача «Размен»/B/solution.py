# Python 3.12.1

n = int(input())
nominal = [1, 5, 10, 20, 50]

numCoins = 0
final = []

for i in nominal[::-1]:
    if n >= i:
        numCoins += n // i
        final += [i] * (n // i)
        n = n % i

print(numCoins)
print(*final)

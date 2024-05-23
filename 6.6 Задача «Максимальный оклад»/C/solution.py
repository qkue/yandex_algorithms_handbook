# Python 3.12.1

r, c = map(int, input().split())

kings = 0
if r * c < 2:
    kings = 0
elif r == 1 or c == 1:
    temp = max(r, c)
    if temp % 3 != 0:
        kings += temp - (temp // 3 + 1)
    else:
        kings += temp - (temp // 3) 
else:
    r_full = r - (r // 3 + [0, 1][r % 3 != 0])
    r_empty = r - r_full
    fill_row = c - (c // 3 + [0, 1][c % 3 != 0])
    kings = r_full * c + r_empty * fill_row
print(kings)

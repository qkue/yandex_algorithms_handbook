# Python 3.12.1

n = int(input())
ax = list(map(int, input().split()))
#ax.sort()

def major(a):
    count = 0
    candidate = 0
    for person in a:
        if count == 0:
            candidate = person
            count += 1
        else:
            if person == candidate:
                count += 1
            else:
                count -= 1
    return (1 if count else 0)
print(major(ax))

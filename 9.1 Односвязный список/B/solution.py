# Python 3.12.1
# Нужно было решить на односвязном списке, но мне хотелось сделать без него. В принципе, делается аналогично

n = int(input())
arr  = list(map(int, input().split()))

min_element = 0
max_element = 1
min_not_approved = 0

# left walk search min left and max right
for num in range(2, n):
    if arr[num] > arr[max_element] or (arr[num] - arr[min_not_approved] > arr[max_element] - arr[min_element]):
        if arr[max_element] < arr[min_element]:
            min_element = max_element
        
        if arr[min_element] > arr[min_not_approved]:
            min_element = min_not_approved
        max_element = num

    elif arr[num] < arr[min_element] and arr[num] < arr[min_not_approved]:
        min_not_approved = num

print(min_element + 1, max_element + 1)

# right walk search max left and min right
min_element = 1
max_element =  0
max_not_approved = 0

for num in range(2, n):
    if arr[num] < arr[min_element] or (arr[max_not_approved] - arr[num] > arr[max_element] - arr[min_element]):
        if arr[min_element] > arr[max_element]:
            max_element = min_element
        
        if arr[max_element] < arr[max_not_approved]:
            max_element = max_not_approved
        min_element = num

    elif arr[num] > arr[max_element] and arr[num] > arr[max_not_approved]:
        max_not_approved = num
    

print(max_element + 1, min_element + 1)

# Python 3.12.1

word_one = input()
word_two = input()
word_one = 'x' + word_one # Чтобы не проставлять единички
word_two = 'x' + word_two 

# table = [[0] * len(word_one) for _ in range(len(word_two))]
table = []
for row in range(len(word_one)):
    temp_list = []
    for col in range(len(word_two)):
        if row == 0:
            temp_list.append(col)
        elif col == 0:
            temp_list.append(row)
        else:
            temp_list.append(0)
    table.append(temp_list)

for row in range(1, len(word_one)):
    for col in range(1, len(word_two)):
        match = table[row - 1][col - 1]
        mismatch = table[row - 1][col - 1] + 1
        insertion = table[row][col - 1] + 1
        deletion = table[row - 1][col] + 1
        if word_one[row] == word_two[col]:
            table[row][col] = min(match, insertion, deletion)
        else:
            table[row][col] = min(mismatch, insertion, deletion)

print(table[row][col])


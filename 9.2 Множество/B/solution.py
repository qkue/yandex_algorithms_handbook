# Python 3.12.1
# Как решить применяя множества без словарей, придумать не получилось

from sys import stdin

n = int(stdin.readline().rstrip())

answer = 0
prepared_input = [0] * n

for i in range(n):
    text = stdin.readline().rstrip()
    temp = [0] * (len(text) + 1)
    for j in range(len(text)):
        temp[j] = text[:j] + text[j + 1:]
    temp[len(text)] = text
    prepared_input[i] = temp


for seg in range(len(prepared_input[0])):
    suffixs_set = set()
    suffixs = dict()
    words = set()
    words_dict = dict()

    for suff in prepared_input:
        suffix = suff[seg]
        word = suff[-1]
        if suffix in suffixs_set:
            repeats = 0
            if word in words:
                repeats = words_dict.get(word)
            answer += (suffixs[suffix] - repeats)
        else:
            suffixs_set.add(suffix)
    
        suffixs[suffix] = suffixs.get(suffix, 0) + 1
        words.add(word)
        words_dict[word] = words_dict.get(word, 0) + 1

print(answer)  

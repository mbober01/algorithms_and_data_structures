def algorytm_naiwny(word, pattern):
    l = len(pattern)
    if l > len(word):
        return False
    index = 0
    where = []
    for i in range(len(word)):
        index = 0
        is_in = True
        for j in range(i, l+i):
            if word[j] == pattern[index]:
                index += 1
                continue
            is_in = False
            break
        if is_in:
            where.append(i)

    if where:
        return where

    return False

print(algorytm_naiwny("abcdab", "ab"))
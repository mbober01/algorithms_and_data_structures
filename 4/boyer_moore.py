def algorytm_boyer_moore(word, pattern):
    l = len(pattern)
    j = l - 1
    i = j
    p = {k:l-pattern[::-1].index(k)-1 for k in pattern}
    where = []
    while i < len(word):
        if word[i] == pattern[j]:
            i -= 1
            j -= 1
        else:
            if word[i] in pattern:
                i = i + l - min(j,1+p[word[i]] )
            else:
                i = i + l
            j = l - 1

        if j == 0:
            where.append(i)
            i = i + l - min(j, 1 + p[word[i]])
        
    if where:
        return where

    return False


print(algorytm_boyer_moore("abdgabgfdabhfdbab", "ab"))
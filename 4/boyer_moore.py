def algorytm_boyer_moore(word, wzorzec):
    l = len(wzorzec)
    j = l - 1
    i = j
    p = {k:l-wzorzec[::-1].index(k)-1 for k in wzorzec}
    where = []
    while i < len(word):
        if word[i] == wzorzec[j]:
            i -= 1
            j -= 1
        else:
            if word[i] in wzorzec:
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
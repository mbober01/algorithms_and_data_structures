def algorytm_naiwny(word, wzorzec):
    l = len(wzorzec)
    if l > len(word):
        return False
    index = 0
    where = []
    for i in range(len(word)):
        index = 0
        is_in = True
        for j in range(i, l+i):
            if word[j] == wzorzec[index]:
                index += 1
                continue
            is_in = False
            break
        if is_in:
            where.append(i)

    if where:
        return where

    return False

def algorytm_2(word, wzorzec):
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

def hash_fun(word, r, p, q):
    m = len(word) - 1
    hw = 0
    for x in word:
        hw += p[x] * pow(r, m)
        # print(f"px = {p[x]}")
        m -= 1
    hw %= q

    return hw
    
def algorytm_karp_rabin(word, wzorzec):
    r = len(set(word))
    m = len(wzorzec)
    p = {a:i for (a,i) in zip(set(word),range(r))}
    q = 11
    i = 0
    where = []
    hw = hash_fun(wzorzec, r, p, q)

    for i in range(len(word)-m+1):
        if i == 0:
            h = hash_fun(word[:len(wzorzec)], r, p, q)
        else:
            h = ((h - (p[word[i - 1]] * pow(r,m-1))) * r + p[word[i+m-1]])
            h %= q
        if h == hw:
            if wzorzec == word[i:i+len(wzorzec)]:
                where.append(i)
    if where:
        return where
    return False


# print(algorytm_naiwny("abcdab", "ab"))
# print(algorytm_2("abdgabgfdabhfdbab", "ab"))
print(algorytm_karp_rabin("abacdcbdacd", "acdc"))

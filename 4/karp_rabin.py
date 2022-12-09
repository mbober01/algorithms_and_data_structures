def hash_fun(word, r, p, q):
    m = len(word) - 1
    hw = 0
    for x in word:
        hw += p[x] * pow(r, m)
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


print(algorytm_karp_rabin("abacdcbdacd", "acdc"))
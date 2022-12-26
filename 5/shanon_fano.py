from itertools import combinations
import time

# to get the key with given val(p)
def get_key(val, tab):
    for key, value in tab.items():
        if val == value:
            return key

# update codes for letters
def update(half1,half2,tab,codes):
    for p in half1:
        codes[get_key(p,tab)].append("1")
    for p in half2:
        codes[get_key(p,tab)].append("0")
    
    return codes

# split in two halves
def split_in_two(probabilities,halves):
    all_combinations= []
    for x in range(1,len(probabilities)):
        c = list(combinations(probabilities, x))
        all_combinations.append(c)

    min_dif = 1
    half1 = 0
    for com in all_combinations:
        for x in com:
            dif = abs(sum(probabilities)/2-sum(list(x)))
            if dif < min_dif:
                min_dif = dif
                half1 = list(x)

    half2 = probabilities[:]
    for p in half1:
        if p in half2:
            half2.remove(p)
    halves.append(half1)
    halves.append(half2)
    
    return half1, half2, halves

# get the code for each letter
def get_code(alphabet, probabilities):
    tab = dict(zip(alphabet,probabilities))
    tab = dict(sorted(tab.items(), key=lambda x:x[1], reverse=True))
    codes = {k: [] for k in tab.keys()}
    # from here on splitting into two equal parts
    halves = []
    half1,half2,halves = split_in_two(probabilities,halves)
    codes = update(half1,half2,tab,codes)
    temp = []
    # keep splitting until there are only lists of each probability
    while len(halves) != len(probabilities):
        temp = [x for x in temp if len(x) == 1]
        for half in halves:
            if len(half) > 1:
                half1,half2,temp = split_in_two(half,temp)
                codes = update(half1,half2,tab,codes)
        halves = temp[:]
    return codes

def encode_text(text, codes):
    encoded_text = ""
    for letter in text:
        encoded_text += "".join(codes[letter])
    return encoded_text


alphabet = ['a','b','c','d','e','f','g','h']
probabilities = [0.01,0.32,0.04,0.06,0.09,0.1,0.15,0.23]
codes = get_code(alphabet,probabilities)
print(codes)
text = "gadac"
encoded_text = encode_text(text, codes)
print(encoded_text)
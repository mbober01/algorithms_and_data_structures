# to get all keys which have given value(p)
def get_key(val, tab):
    binary = []
    for key, value in tab.items():
        if val == value:
            binary.append(key)
    return binary

# two smallest probabilities
def two_smallest(p):
    p = sorted(p)
    x = p[0]
    p.pop(0)
    y = p[0]
    p.pop(0)
    p.insert(0, round(x+y,4))
    return x, y, p

# codes for each letter
def get_code(alphabet, probability):
    tab = dict(zip(alphabet,probability))
    tab = dict(sorted(tab.items(), key=lambda x:x[1], reverse=True)) # alphabet with probabilities for each letter
    p = list(tab.values()) # probabilities for change
    codes = {k: [] for k in tab.keys()} # codes for letters
    # p will have the tree with updates probabilities and will end with only 1.0 at the end thats when algorithm stops
    while len(p) > 1:
        x, y, p = two_smallest(p)
        keys_x = get_key(x, tab)
        keys_y = get_key(y, tab)
        new_p = round(x + y,4)
        # update values
        if keys_x == keys_y:
            keys_x = keys_x[1:]
            keys_y = [keys_y[0]]
        to_update = keys_x + keys_y
        for key in to_update:
            tab[key] = new_p
        for key in keys_x:
            codes[key].append("1")
        for key in keys_y:
            codes[key].append("0")
    return codes
      
# encode the given text based on codes for each letter (text must consist only letters that have their codes)        
def encode_text(text, codes):
    encoded_text = ""
    for letter in text:
        encoded_text += "".join(codes[letter])
    return encoded_text
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
probability = [0.13, 0.07, 0.25, 0.04, 0.23, 0.28]
codes = get_code(alphabet,probability)
print(codes)
text = "dabef"
encoded_text = encode_text(text, codes)
print(encoded_text)

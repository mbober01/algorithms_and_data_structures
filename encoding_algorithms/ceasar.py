def caesar(shift,text):
    shift %=26
    return [chr((ord(x)+shift-65) % 26 + 65) if x.isupper() else chr((ord(x)+shift-97) % 26 + 97) for x in text]

text = "ABCDabcd"
shift = 4
print("".join(caesar(shift, text)))
#max num
def max_num(nums):
    nums = [float(x) for x in nums.split(";")]
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    return max
# xd testowanie
#to rpn
def to_rpn(calc):
    prio = {
        '(':0,
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3
    }

    stack = []

    output = ""
    #to rpn
    for elem in calc:
        if elem.isnumeric():#jesli liczba dodaj do wyjscia
            output += elem

        elif elem == "(":# jesli ( dodaj do stosu
            stack.append(elem)

        elif elem == ")":# jesli ) dodawaj elementy  ze stosu do wyjscia  az kolejnym elementem na stosie bedzie )
            while stack[-1] != "(":
                output += stack.pop()
            stack.pop()# usun ) ze stosu

        elif elem in prio.keys(): # jesli to symbol znajdujacy sie w kluczach slownika "prio"
            if len(stack) == 0: # jesli stos jest pusty dodaj do stosu 
                stack.append(elem)

            else:
                while prio[stack[-1]] >= prio[elem] and len(stack)>0: # dodawaj do wyjscia tak dlugo jak ostatni element stosu ma priorytet wiekszy lub
                    output += stack.pop()                             # rowny priorytetowi aktualnego elementu i dlugosc stosu jest wieksza od 0
        
                stack.append(elem)

    for elem in stack: # dodaj do wyjscia wszystko co zostalo na stosie
        output += elem

    return output


#from rpn
def from_rpn(calc):
    stack = []
    for elem in calc: 
        if elem.isnumeric(): # jesli liczba to dodaj do stosu
            stack.append(elem)

        else: # else wez przedostatni i ostatni element stosu a pomiedzy nie dodaj znak 
            operation = f"({stack[-2]} {elem} {stack[-1]})" 
            stack.pop() # wywal dwa ostatni elementy 
            stack.pop()
            stack.append(operation) # dodaj na szczyt stosu nowa czesc dzialania

    return stack[0] # wypisz dzialanie


print(max_num("1;3;5;2;2.1"))
print(to_rpn("((4+2)/3+(2-1))-2"))
print(from_rpn("42+3/21-+2-"))



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
    for elem in calc:
        if elem.isnumeric():
            output += elem

        elif elem == "(":
            stack.append(elem)

        elif elem == ")":
            while stack[-1] != "(":
                output += stack.pop()
            stack.pop()

        elif elem in prio.keys(): 
            if len(stack) == 0: 
                stack.append(elem)

            else:
                while prio[stack[-1]] >= prio[elem] and len(stack)>0: 
                    output += stack.pop()                             
        
                stack.append(elem)

    for elem in stack: 
        output += elem

    return output

print(to_rpn("((4+2)/3+(2-1))-2"))
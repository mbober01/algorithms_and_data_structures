def from_rpn(calc):
    stack = []
    for elem in calc: 
        if elem.isnumeric(): 
            stack.append(elem)

        else: 
            operation = f"({stack[-2]} {elem} {stack[-1]})" 
            stack.pop()  
            stack.pop()
            stack.append(operation) 

    return stack[0]

print(from_rpn("42+3/21-+2-"))
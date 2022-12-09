class Stack:
    
    def __init__(self,length):
        self.t = [0 for x in range(length)]
        self.length = length
        self.index = 0
    
    def __repr__(self):
        return " ".join([str(x) for x in self.t]) + f"  index = {self.index}"

    def add(self, x):
        if self.index == self.length:
            return "Stack full"
        self.t[self.index] = x
        self.index += 1
        return f"added {x} to stack at index {self.index-1}"
    
    def remove(self):
        self.index -= 1
        return f"removed last item from stack\ncurrent index = {self.index}"
        
    
    def check_if_in(self, x):
        return any([elem == x for elem in self.t])

    def top_item(self):
        return self.t[self.index-1]
    

def test_stack():
    stack = Stack(5)
    print(stack.add(1))
    print(stack.add(2))
    print(stack.remove())
    print(stack.add(3))
    print(stack.add(4))
    print(stack.add(9))
    print(stack)
    print(stack.check_if_in(4))
    print(stack.top_item())

test_stack()
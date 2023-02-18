class Queue:
    
    def __init__(self,length):
        self.length = length
        self.t = [0 for x in range(length)]
        self.add_index = 0
        self.rem_index = 0
    
    def __repr__(self):
        return " ".join([str(x) for x in self.t]) + f"  add_index = {self.add_index}, rem_index = {self.rem_index}"

    def add(self, x):
        if self.add_index == self.rem_index and self.t[self.add_index] != 0:
            return "queue is full "
        elif self.add_index == self.length:
            self.add_index = 0
        self.t[self.add_index] = x
        self.add_index += 1
        return f"added {x} to stack "
    
    def remove(self):
        if self.rem_index == self.length:
            self.rem_index = 0
        self.t[self.rem_index] = 0
        self.rem_index += 1
        return f"removed item from stack current rem_index = {self.rem_index}"
    
    def check_if_in(self, x):
        return any([elem == x for elem in self.t])
    
    def top_item(self):
        return self.t[self.rem_index-1]


def test_queue():
    queue = Queue(4)
    print(queue.add(1))
    print(queue.add(2))
    print(queue.remove())
    print(queue.add(3))
    print(queue.add(4))
    print(queue)


test_queue()
class PrioQueue:
    def __init__(self, length):
        self.length = length
        self.t = [0 for x in range(length)]
        self.add_index = 0
        self.rem_index = 0
        self.help_index = 0
    
    def __repr__(self):
        return " ".join([str(x) for x in self.t]) + f"  add_index = {self.add_index}, rem_index = {self.rem_index}"
    
    def add(self, x):
        if self.add_index == self.rem_index and self.t[self.add_index] != 0:
            return "prio queue is full "
        elif self.add_index == self.length:
            self.add_index = 0
        self.t[self.add_index] = x
        self.add_index += 1
        return f"added {x} to the prio_queue"

    def remove(self):
        if self.rem_index == self.length:
            self.rem_index = 0
        
        self.help_index = self.find_smallest()
        self.t[self.help_index], self.t[self.rem_index] = self.t[self.rem_index], self.t[self.help_index]
        self.t[self.rem_index] = 0
        self.rem_index += 1
        return f"removed item from prio_queue"
        
    def check_if_in(self, x):
        return any([elem == x for elem in self.t])

    def top_item(self):
        return f"top item to remove {self.t[self.find_smallest]}"
    
    def find_smallest(self):
        min = max(self.t)
        help_index = 0
        for i in range(self.length):
            if self.t[i] < min and self.t[i] != 0:
                min = self.t[i]
                help_index = i
        return help_index


def test_prio_queue():
    prio_queue = PrioQueue(4)
    print(prio_queue.add(1))
    print(prio_queue.add(2))
    print(prio_queue)
    print(prio_queue.remove())
    print(prio_queue)
    print(prio_queue.add(1))
    print(prio_queue)
    print(prio_queue.add(1))
    print(prio_queue)
    print(prio_queue.remove())
    print(prio_queue)

test_prio_queue()
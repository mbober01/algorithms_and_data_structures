class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def add_at(self, data, index):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            new_node = Node(data)
            if index != 0:
                try:
                    for i in range(index):
                        if i == index - 1:
                            temp = current.next
                            current.next = new_node
                            new_node.next = temp
                            break
                        current = current.next
                except AttributeError:
                    self.add(data)
            else:
                self.head = new_node
                new_node.next = current

    def remove(self, index):
        current = self.head
        prev = None
        ind = 0
        while current.next:
            prev = current
            current = current.next
            ind += 1
            if ind == index: break
        prev.next = current.next

    def check_if_in(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def current_item(self):
        current = self.head
        while current.next:
            current = current.next
            if not current.next:
                return current.data





        




lista = LinkedList()
lista.add(0)
lista.add(1)
lista.add(3)
lista.add_at(2, 1)
lista.add_at(8,9)
lista.remove(2)
lista.show()
print(f"czy 6 jest w liscie:  {lista.check_if_in(6)}")
print(f"otatnia pozycja w liscie to: {lista.current_item()}")

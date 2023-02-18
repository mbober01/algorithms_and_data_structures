class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current.prev = current
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def add_at(self, data, index):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            if index != 0:
                try:
                    for i in range(index):
                            if i == index -1:
                                new_node.next = current.next
                                new_node.prev = current
                                current.next = new_node
                                break
                            current = current.next
                except AttributeError:
                    self.add(data)
            else:
                self.head = new_node
                new_node.next = current

    def show(self):
        last = self.head
        while last:
            print(last.data)
            last = last.next

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
        current.prev = prev
    
    def check_if_in(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def last_item(self):
        current = self.head
        while current:
            current = current.next
            if not current.next:
                return current.data
            
    
lista = DoublyLinkedList()
lista.add(0)
lista.add(1)
lista.add(3)
lista.add_at(2,2)
lista.remove(1)
lista.show()
print(f"czy 6 jest w liscie:  {lista.check_if_in(6)}")
print(f"otatnia pozycja w liscie to: {lista.last_item()}")






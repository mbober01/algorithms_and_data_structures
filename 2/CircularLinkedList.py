

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:  
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head: break
            

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
                if current == self.head: break
            current.next = new_node
            new_node.next = self.head

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
            if ind == index:
                break
            prev = current
            current = current.next
            ind += 1
            if current.next == self.head:
                break
        prev.next = current.next

    def check_if_in(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
            if current == self.head: break
        return False

    def current_item(self):
        current = self.head
        while current:
            current = current.next
            if current.next == self.head:
                return current.data

lista = circularLinkedList()

print("Elements are added to the list ")
lista.add_at(0,0)
lista.add_at(1,1)
lista.add_at(2,2)
lista.add_at(9,9)
lista.remove(3)
lista.show()
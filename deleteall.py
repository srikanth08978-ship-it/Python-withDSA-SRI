class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteall(self, data):
        if self.head is None:
            return
        while self.head is not None and self.head.data == data:
            self.head = self.head.next
        cn = self.head
        while cn is not None and cn.next is not None:
            if cn.next.data == data:
                cn.next = cn.next.next
            else:
                cn = cn.next

    def display(self):
        """Helper method to print the list."""
        elements = []
        cn = self.head
        while cn:
            elements.append(str(cn.data))
            cn = cn.next
        print(" -> ".join(elements) if elements else "Empty List")

ll = LinkedList()

for value in:
    ll.append(value)

print("Original list:")
ll.display()


ll.deleteall(30)

print("\nAfter deleting all 30s:")
ll.display()  

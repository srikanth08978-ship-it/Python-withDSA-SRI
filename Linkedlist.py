class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def add(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    # Display linked list
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("None")

    # Search element
    def search(self, data):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == data:
                print("data is at", pos, "found")
                return
            temp = temp.next
            pos += 1

        print("data not found")

    # Delete a particular value
    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    # Find length
    def length(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        print(count)

    # Insert at beginning
    def insertatbeg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # Delete last node
    def deletelast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete node at given index
    def delAt(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            if temp.next is None:
                return
            temp = temp.next

        if temp.next is not None:
            temp.next = temp.next.next



    def deleteall(self, data):
    cn = self.head
    while cn is not None and cn.next is not None:
        if cn.next.data == data:
            cn.next = cn.next.next
            self.size -= 1
        else:
            cn = cn.next  
    if self.head is not None and self.head.data == data:
        self.head = self.head.next
        self.size -= 1


# Main
ll = LinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(44)
ll.add(7667)

ll.traverse()
ll.search(10)
ll.delete(10)
ll.length()

ll.insertatbeg(90)
ll.deletelast()
ll.traverse()

ll.delete(30)
ll.traverse()

ll.add(30)
ll.add(44)
ll.add(7667)

ll.delAt(2)
ll.traverse() 

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head == None:
            print("Empty Node")
        while self.head:
            suffix=" "
            if self.head.next!=None:
                suffix = "-->"
            print(str(self.head.value),end=suffix)
            self.head=self.head.next
obj = SingleLinkedList()
node1=Node(1)
obj.head=node1

node2=Node(2)
obj.head.next=node2

node3=Node(3)
node2.next=node3

obj.display()
            
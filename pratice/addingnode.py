class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newnode
    def printlist(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next

linkedlist1=linkedlist()
linkedlist1.add(10)
linkedlist1.add(20)
linkedlist1.add(30)
linkedlist1.printlist()
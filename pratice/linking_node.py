class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
node2=node(20)
node3=node(30)
head.next=node2
node2.next=node3

current=head
while current is not None:
    print(current.data)
    current=current.next
print(current)

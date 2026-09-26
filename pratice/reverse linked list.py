class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
head=listnode(10)
head.next=listnode(20)
head.next.next=listnode(30)
head.next.next.next=listnode(40)
current=head
previous=None
while current is not None:
    nextnode=current.next
    current.next=previous
    previous=current
    current=nextnode
head=previous

while head is not None:
    print(head.val)
    head=head.next
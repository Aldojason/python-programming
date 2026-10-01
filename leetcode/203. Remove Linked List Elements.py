class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
head=listnode(1)
head.next=listnode(2)   
head.next.next=listnode(6)
head.next.next.next=listnode(3)
head.next.next.next.next=listnode(4)
head.next.next.next.next.next=listnode(5)
head.next.next.next.next.next.next=listnode(6)
def remove_elements(head,target):
    if head is None:
        return head
    while head is not None and head.val==target:
        head=head.next
    current=head
    previous=head
    while current is not None:
        if current.val==target:
            previous.next=current.next
            current=current.next
        else:
            previous=current
            current=current.next
    return head
result=remove_elements(head,6)
while result is not None:
    print(result.val,end=" ")
    result=result.next
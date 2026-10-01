class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
head=listnode(1)
head.next=listnode(1)
head.next.next=listnode(2)
head.next.next.next=listnode(3)
head.next.next.next.next=listnode(3)
def remove_duplicates(head):
    current=head
    if current is None:
        return head
    while current.next is not None:
        if current.val==current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return head
result=remove_duplicates(head)
while result is not None:
    print(result.val)
    result=result.next
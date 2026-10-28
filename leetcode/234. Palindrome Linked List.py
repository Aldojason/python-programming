class listNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
head=listNode(1)
head.next=listNode(2)
head.next.next=listNode(2)
head.next.next.next=listNode(1)
def palindrome_linked_list(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    if fast is not None:
        slow=slow.next
    previous=None
    while slow is not None:
        next_node=slow.next
        slow.next=previous
        previous=slow
        slow=next_node
    while previous is not None:
        if head.val!=previous.val:
            return False
        head=head.next
        previous=previous.next
    return True
result=palindrome_linked_list(head)
print(result)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow.next
        slow.next=None

        while curr :
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        newHead=prev

        dummy=ListNode()
        curr=dummy

        while head and newHead :
            curr.next=head
            head=head.next
            curr=curr.next
            curr.next=newHead
            newHead=newHead.next
            curr=curr.next
        
        if head :
            curr.next=head
        if newHead :
            curr.next=newHead




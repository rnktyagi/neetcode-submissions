# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr :
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        newHead=prev

        if n==1 :
            newHead=newHead.next

        else :
            curr=newHead
            for i in range(n-2) :
                curr=curr.next
            
            curr.next=curr.next.next

        P=None
        C=newHead

        while C :
            temp=C.next
            C.next=P
            P=C
            C=temp
        
        return P
        
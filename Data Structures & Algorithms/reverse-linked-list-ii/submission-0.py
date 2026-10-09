# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left==1 :
            before=None
            curr=head
            for i in range(1,right) :
                curr=curr.next
            
            after=curr.next
            curr.next=None

            curr=head
            prev=None
            
            while curr :
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            head.next=after

            head=prev

            return head
        
        else :

            curr=head
            before=None
            after=None

            for i in range(1,right) :
                if i==left-1 :
                    before=curr
                curr=curr.next
            
            after=curr.next

            curr.next=None

            start=before.next
            before.next=None
            
            prev=None

            while start :
                temp=start.next
                start.next=prev
                prev=start
                start=temp
            
            before.next=prev

            while prev.next :
                prev=prev.next
            
            prev.next=after

            return head



            



        
        
        
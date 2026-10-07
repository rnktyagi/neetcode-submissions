# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        curr=dummy
        carry=0

        while l1 and l2:
            value = l1.val + l2.val + carry

            actual = value % 10
            carry = value // 10

            toAdd = ListNode(actual)

            curr.next = toAdd
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            value = l1.val + carry

            actual = value % 10
            carry = value // 10

            toAdd = ListNode(actual)

            curr.next = toAdd
            curr = curr.next

            l1 = l1.next

        while l2:
            value = l2.val + carry

            actual = value % 10
            carry = value // 10

            toAdd = ListNode(actual)

            curr.next = toAdd
            curr = curr.next

            l2 = l2.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next

        
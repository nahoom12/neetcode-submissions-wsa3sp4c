# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        current = slow.next
        slow.next = None
        prev = None
        Next = None
        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        l1 = head
        l2 = prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1,l2 = temp1,temp2


        
        
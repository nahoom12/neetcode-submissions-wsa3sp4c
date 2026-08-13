# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp!= None:
            temp = temp.next
            count += 1
        pivot = count - n
        curr = head
        prev = ListNode()
        dummy = prev
        while pivot != 0:
            dummy.next = curr
            curr = curr.next
            pivot -= 1
            dummy = dummy.next
        dummy.next = curr.next
        curr.next = None
        return prev.next







        
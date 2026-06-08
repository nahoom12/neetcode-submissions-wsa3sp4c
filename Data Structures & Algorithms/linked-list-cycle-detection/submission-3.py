# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        if slow and slow.next  == None or slow == None:
            return False
        fast = slow.next.next
        while slow != fast:
            slow = slow.next
            if fast == None or fast.next == None or fast.next.next == None:
                return False
            fast = fast.next.next
        return True

        
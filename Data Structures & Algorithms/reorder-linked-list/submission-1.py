# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast= head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            Nextcurr = second.next
            second.next = prev
            prev = second
            second = Nextcurr
        first,last = head,prev
        while last:
            temp1,temp2 = first.next,last.next
            first.next = last
            last.next = temp1
            first,last = temp1,temp2
        

        
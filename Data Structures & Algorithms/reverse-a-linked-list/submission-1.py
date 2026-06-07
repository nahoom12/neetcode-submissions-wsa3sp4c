# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''prev = None
        currNext = None
        curr = head
        if head == None:
            return head
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        return prev'''
        #Recursive approach 
        #uses the base case and builds the  linked list up 
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


            
        
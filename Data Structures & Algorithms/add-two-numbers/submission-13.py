# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        dummy = ListNode()
        start.next = dummy
        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit >= 10:
                digit = digit - 10
                dummy.val = digit
                carry = 1
            else:
                dummy.val = digit
                carry = 0
            l1 = l1.next
            l2 = l2.next
            dummy.next = ListNode()
            dummy = dummy.next
        if not l1 and not  l2:
            if carry:
                dummy.val = carry
                dummy.next = None
                return start.next
        while l1:
            digit = l1.val + carry
            if digit >= 10:
                digit = digit - 10
                dummy.val = digit
                carry = 1
            else:
                dummy.val= digit
                carry = 0
            dummy.next = ListNode()
            l1 = l1.next
            dummy = dummy.next
        while l2:
            digit = l2.val + carry
            if digit >= 10:
                digit = digit - 10
                dummy.val = digit
                carry = 1
            else:
                dummy.val= digit
                carry = 0
            dummy.next = ListNode()
            l2 = l2.next
            dummy = dummy.next
        if carry:
            dummy.val = carry
            return start.next
        else:
            temp = start.next
            lol = temp
            while lol.next.next != None:
                lol = lol.next
            lol.next = None
            return temp
            
       

            
        
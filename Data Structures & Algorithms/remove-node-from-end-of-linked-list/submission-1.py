# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count,rmv = 0,0
        dummy = head
        while dummy != None:
            dummy = dummy.next
            count +=1
        index = count - n
        if index == 0:
            head = head.next
            return head
        dummy2 = head
        ret = dummy2
        while rmv != index - 1:
            dummy2 = dummy2.next
            rmv += 1
        if dummy2.next:
            dummy2.next = dummy2.next.next
        else:
            return None
        last = dummy2.next
        while last != None:
            last = last.next    
        return ret


        
        
        
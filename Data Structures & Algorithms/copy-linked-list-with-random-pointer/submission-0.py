"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocurr = { None:None }
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtocurr[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldtocurr[curr]
            copy.next = oldtocurr[curr.next]
            copy.random = oldtocurr[curr.random]
            curr = curr.next
        return oldtocurr[head]




        
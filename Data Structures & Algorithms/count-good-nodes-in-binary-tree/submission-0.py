# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
    def dfs(self,node,max_sofar):
        if node == None:
            return 0
        if node.val >= max_sofar:
            good = 1
        else:
            good = 0
        max_sofar = max(node.val,max_sofar)
        return good + self.dfs(node.right,max_sofar) + self.dfs(node.left,max_sofar)
                

            

        

     
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_sofar):
            if root == None:
                return  0
            if root.val >= max_sofar:
                good = 1
            else:
                good = 0
            max_sofar = max(root.val,max_sofar)
            left = dfs(root.left,max_sofar)
            right = dfs(root.right,max_sofar)
            return good + left + right
        return dfs(root,root.val)
        

            
            
        

        
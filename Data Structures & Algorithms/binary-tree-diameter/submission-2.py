# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(p):
            if p == None:
                return 0
            left =  dfs(p.left)
            right = dfs(p.right)
            self.diameter = max(self.diameter,left + right)
            return max(left,right) + 1
        dfs(root) 
        return self.diameter   
        
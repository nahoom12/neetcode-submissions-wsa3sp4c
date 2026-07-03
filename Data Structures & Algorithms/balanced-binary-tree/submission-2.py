# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(p):
            if p == None:
                return 0
            left = dfs(p.left)
            right = dfs(p.right)
            #comparsion
            if abs(left - right) > 1:
                self.is_balanced = False
            return max(left,right) + 1
        dfs(root)
        return self.is_balanced

        
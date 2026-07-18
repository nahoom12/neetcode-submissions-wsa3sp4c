# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")
        def path_sum(node):
            if node is None:
                return 0
            left = max(path_sum(node.left),0)
            right = max(path_sum(node.right),0)
            current_max = node.val + left + right
            self.max_path = max(self.max_path,current_max)
            return node.val + max(left,right)
        path_sum(root)
        return self.max_path


        
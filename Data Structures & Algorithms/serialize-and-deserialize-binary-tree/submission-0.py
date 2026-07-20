# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = []
        def dfs(node):
            if node is None:
                self.string.append("N")
                self.string.append(",")
                return None
            x = node.val
            self.string.append(str(x))
            self.string.append(",")
            left = dfs(node.left)
            right = dfs(node.right)
            return root
        dfs(root)
        return "".join(self.string)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(vals[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            
            



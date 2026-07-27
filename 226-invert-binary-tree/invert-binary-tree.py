class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right=root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
root=TreeNode(4)
root=TreeNode(2, TreeNode(3), TreeNode(1))
root=TreeNode(7, TreeNode(9), TreeNode(6))
sol=Solution()
print(sol.invertTree(root))
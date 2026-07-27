class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return 1+max(left_depth,right_depth)
root=TreeNode(3)
root.left=TreeNode(9)
root.rigth=TreeNode(20)
root.rigth.left=TreeNode(15)
root.rigth.rigth=TreeNode(7)

sol=Solution()
print(sol.maxDepth(root))
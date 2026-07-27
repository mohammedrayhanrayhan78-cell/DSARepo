class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return (self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val))
root=TreeNode(5)
root.left=TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right=TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
sol=Solution()
print(sol.hasPathSum(root, 22))
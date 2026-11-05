# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(left_idx: int, right_idx: int)->TreeNode|None:
            if left_idx > right_idx:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.right = helper(mid + 1, right_idx)
            root.left = helper(left_idx, mid - 1)
            return root
        return helper(0, len(inorder)-1)
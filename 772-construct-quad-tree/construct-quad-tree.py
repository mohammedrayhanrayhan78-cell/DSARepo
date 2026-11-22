"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def get_uniform_value(row: int, col: int, size: int):
            target = grid[row][col]
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != target:
                        return None
            return target
        def build(row: int, col: int,size: int)->'Node':
            uniform_val = get_uniform_value(row, col, size)
            if uniform_val is not None:
                return Node(
                    val = bool(uniform_val),
                    isLeaf = True,
                    topLeft = None,
                    topRight = None,
                    bottomLeft = None,
                    bottomRight = None,
                )
            half = size // 2
            top_left = build(row, col, half)
            top_right = build(row, col + half, half)
            bottom_left = build(row + half, col, half)
            bottom_right = build(row + half, col + half, half)
            return Node(
                val = True,
                isLeaf = False,
                topLeft = top_left,
                topRight = top_right,
                bottomLeft = bottom_left,
                bottomRight = bottom_right
            )
        return build(0,0,len(grid))
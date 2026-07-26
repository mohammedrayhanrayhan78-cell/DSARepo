class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        max_depth=0
        for char in s:
            if char == '(':
                depth+=1
            if depth>max_depth:
                max_depth=depth
            elif char == ')':
                depth-=1
        return max_depth
s = "(1)+((2))+(((3)))"
sol=Solution()
print(sol.maxDepth(s))
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s+s)
s = "abcde"
goal = "cdeab"
sol=Solution()
print(sol.rotateString(s,goal))
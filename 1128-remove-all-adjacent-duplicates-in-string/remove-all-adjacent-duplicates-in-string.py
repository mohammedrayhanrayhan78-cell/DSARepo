class Solution:
    def removeDuplicates(self, s: str) -> str:
        word=list(s)
        stack=[]
        for char in word:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
            pass
        return "".join(stack)
s = "abbaca"
sol=Solution()
print(sol.removeDuplicates(s))


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word=list(s)
        left, right = 0, len(word)-1
        while left<right:
            while left<right and not word[left] .isalpha():
                left+=1
            while left<right and not word[right] .isalpha():
                right-=1
            word[left], word[right]=word[right], word[left]
            left+=1
            right-=1
        return "".join(word)
s = "ab-cd"
sol=Solution()
print(sol.reverseOnlyLetters(s))
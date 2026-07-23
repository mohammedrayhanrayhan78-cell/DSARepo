class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for char in s:
            if char.isalnum():
                cleaned+=char.lower()

        return cleaned == cleaned[::-1]
s = "A man, a plan, a canal: Panama"
sol=Solution()
print(sol.isPalindrome(s))
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels="aeiouAEIOU"
        half_1=s[:len(s)//2]
        half_2=s[len(s)//2:]
        count_1=0
        for char in half_1:
            if char in vowels:
                count_1+=1
        count_2=0
        for char in half_2:
            if char in vowels:
                count_2+=1
        return count_1 == count_2
s = "book"
sol=Solution()
print(sol.halvesAreAlike(s))
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        for i, char in enumerate(s):
            if freq[char]==1:
                return i
        return -1
s = "leetcode"
sol=Solution()
sol.firstUniqChar(s)
print(sol.firstUniqChar(s))         
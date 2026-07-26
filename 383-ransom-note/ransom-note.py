class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq={}
        for char in magazine:
            if char in magazine_freq:
                magazine_freq[char]+=1
            else:
                magazine_freq[char]=1
        ransom_freq={}
        for char in ransomNote:
            if char in  ransom_freq:
                 ransom_freq[char]+=1
            else:
                 ransom_freq[char]=1
        for char, needed_count in ransom_freq.items():
            if char not in magazine_freq or magazine_freq[char] < needed_count:
                return False
        return True
ransomNote = "a"
magazine = "b"
sol=Solution()
sol.canConstruct(ransomNote, magazine)
print(sol.canConstruct(ransomNote, magazine))
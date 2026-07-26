class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        while word*(k + 1) in sequence:
            k+=1
        return k
sequence = "ababc"
word = "ab"
sol=Solution()
print(sol.maxRepeating(sequence,word))
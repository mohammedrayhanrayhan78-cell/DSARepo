class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq_1={}
        for word in words1:
            if word in freq_1:
                freq_1[word]+=1
            else:
                freq_1[word]=1
        freq_2={}
        for word in words2:
            if word in freq_2:
                freq_2[word]+=1
            else:
                freq_2[word]=1
        count=0
        for word in freq_1:
            if freq_1[word]==1 and freq_2.get(word, 0)==1:
                count+=1
        return count
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
sol=Solution()
print(sol.countWords(words1,words2))
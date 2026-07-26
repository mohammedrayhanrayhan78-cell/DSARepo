class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        word=text.split()
        result=[]
        for i in range(len(word)-2):
            if word[i] == first and word[i+1] == second:
                result.append(word[i+2])
        return result
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
sol=Solution()
print(sol.findOcurrences(text,first,second))
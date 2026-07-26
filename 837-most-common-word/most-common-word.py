class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned=""
        for char in paragraph:
            if char.isalnum() or char == " ":
                cleaned+=char.lower()
            else:
                cleaned+=" "
        words=cleaned.split()
        freq={}
        for word in words:
            if word not in banned:
                if word in freq:
                    freq[word]+=1
                else:
                    freq[word]=1
        max_char=" "
        max_count=0
        for char, count in freq.items():
            if count>max_count:
                max_count=count
                max_char=char
        return max_char
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol=Solution()
print(sol.mostCommonWord(paragraph,banned))

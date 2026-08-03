from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        len_p=len(p)
        count_p=Counter(p)
        window=Counter(s[:len_p])
        if window==count_p:
            res.append(0)
        for i in range(len_p, len(s)):
            left_char=s[i-len_p]
            window[left_char]-=1
            if window[left_char]==0:
                del window[left_char]
            right_char=s[i]
            window[right_char]+=1
            if window==count_p:
                res.append(i-len_p+1)
        return res
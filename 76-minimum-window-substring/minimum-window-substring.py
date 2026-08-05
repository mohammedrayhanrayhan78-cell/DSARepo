from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need=Counter(t)
        have={}
        required=len(need)
        formed=0
        l=0
        ans=(float("inf"), None, None)
        for r, char in enumerate(s):
            have[char]=have.get(char, 0)+1
            if char in need and have[char]==need[char]:
                formed+=1
            while l<=r and formed==required:
                if r-l+1<ans[0]:
                    ans=(r-l+1, l, r)
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
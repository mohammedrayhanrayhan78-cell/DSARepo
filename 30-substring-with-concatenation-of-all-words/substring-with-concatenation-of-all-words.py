from collections import Counter
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []
        for i in range(word_len):
            l = i
            curr_count = Counter()
            for r in range(i, len(s) - word_len + 1, word_len):
                word = s[r:r + word_len]
                if word in word_count:
                    curr_count[word] += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[l:l + word_len]] -= 1
                        l += word_len
                    if r - l + word_len == total_len:
                        res.append(l)
                else:
                    curr_count.clear()
                    l = r + word_len
        return res
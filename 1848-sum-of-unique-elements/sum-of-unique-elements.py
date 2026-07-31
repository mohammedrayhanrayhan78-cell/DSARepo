from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        total = 0
        for num, count in freq.items():
            if count == 1:
                total+=num
        return total
 

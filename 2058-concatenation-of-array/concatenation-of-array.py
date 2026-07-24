class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
nums = [1,2,1]
sol=Solution()
print(sol.getConcatenation(nums))
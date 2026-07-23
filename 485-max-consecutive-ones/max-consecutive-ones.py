class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streaks=0
        current_streak=0
        for num in nums:
            if num == 1:
                current_streak+=1
            else:
                current_streak=0
            max_streaks=max(max_streaks, current_streak)
        return max_streaks
nums = [1,1,0,1,1,1]
sol=Solution()
print(sol.findMaxConsecutiveOnes(nums))
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            digit_count=len(str(num))
            if digit_count%2==0:
                count+=1
        return count
nums = [12,345,2,6,7896]
sol=Solution()
print(sol.findNumbers(nums))
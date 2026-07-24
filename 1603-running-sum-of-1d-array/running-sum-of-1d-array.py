class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count=0
        result=[]
        for num in nums:
            count+=num
            result.append(count)
        return result   
nums = [1,2,3,4]
sol=Solution()
print(sol.runningSum(nums))
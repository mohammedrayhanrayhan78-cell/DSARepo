class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            count=0
            for other in nums:
                if other < num:
                    count+=1
            result.append(count)
        return result
nums = [8,1,2,2,3]
sol=Solution()
print(sol.smallerNumbersThanCurrent(nums))
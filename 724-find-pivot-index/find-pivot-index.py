class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=sum(nums[:i])
            b=sum(nums[i+1:])
            if a==b:
                return i
        return -1
nums = [1,7,3,6,5,6]
sol=Solution()
print(sol.pivotIndex(nums))
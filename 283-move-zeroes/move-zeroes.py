class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_index=0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[i], nums[write_index] = nums[write_index], nums[i]
                write_index+=1
nums = [0,1,0,3,12]
sol=Solution()
sol.moveZeroes(nums)
print(nums)
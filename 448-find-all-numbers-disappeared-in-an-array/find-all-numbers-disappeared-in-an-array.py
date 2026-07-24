class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set(nums)
        result=[]
        for i in range(1, n + 1):
            if i not in seen:
                result.append(i)
        return result
nums = [4,3,2,7,8,2,3,1]
sol=Solution()
print(sol.findDisappearedNumbers(nums))
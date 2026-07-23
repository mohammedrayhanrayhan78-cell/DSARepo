class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        count=0
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for number, times_seen in seen.items():
            if times_seen == 1:
                return number

nums = [2,2,1]
sol=Solution()
print(sol.singleNumber(nums))            
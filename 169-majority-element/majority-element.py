class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for number, times_seen in seen.items():
            if times_seen>len(nums)/2:
                return number
                
nums = [3,2,3]
sol=Solution()
print(sol.majorityElement(nums))

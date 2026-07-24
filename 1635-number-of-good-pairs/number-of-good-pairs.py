class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        total_things=0
        for number, times_seen in seen.items():
            total_things+=times_seen*(times_seen-1)//2
        return total_things
nums = [1,2,3,1,1,3]
sol=Solution()
print(sol.numIdenticalPairs(nums))
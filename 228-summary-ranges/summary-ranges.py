class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result=[]
        i=0
        n=len(nums)
        while i<n:
            start=nums[i]
            j=i
            while j+1<n and nums[j+1]==nums[j]+1:
                j+=1
            if start==nums[j]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[j]}")

            i=j+1
        return result
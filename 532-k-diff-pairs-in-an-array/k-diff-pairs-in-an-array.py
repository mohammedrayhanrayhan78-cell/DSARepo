class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        num_set=set(nums)
        result_set=set()
        for num in nums:
            if k==0:
                if nums.count(num)>1:
                    result_set.add(num)
            else:
                if num + k in num_set:
                    result_set.add(num)
        return len(result_set)
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = nums[0]
        curr_max = nums[0]
        max_subarray_sum = nums[0]
        curr_min = nums[0]
        min_subarray_sum = nums[0]
        for num in nums[1:]:
            total_sum += num
            curr_max = max(num, curr_max + num)
            max_subarray_sum = max(max_subarray_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_subarray_sum = min(min_subarray_sum, curr_min)
        if max_subarray_sum < 0:
            return max_subarray_sum
        return max(max_subarray_sum, total_sum - min_subarray_sum)

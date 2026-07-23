class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=0
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        result=list(common)
        return result
nums1 = [1,2,2,1]
nums2 = [2,2]
sol=Solution()
print(sol.intersection(nums1,nums2))
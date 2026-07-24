class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        result=[]
        for a, b in zip(x,y):
            result.append(a)
            result.append(b)
        return result
nums = [2,5,1,3,4,7]
n = 3
sol=Solution()
print(sol.shuffle(nums,n))
                

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)):
            left_safe = (i == 0) or (flowerbed[i-1]==0)
            right_safe = (i == len(flowerbed) - 1) or (flowerbed[i+1]==0)
            if flowerbed[i] == 0 and left_safe and right_safe:
                flowerbed[i]=1
                count+=1
                if count >= n:
                    return True
        return count>= n
flowerbed = [1,0,0,0,1]
n = 1
sol=Solution()
print(sol.canPlaceFlowers(flowerbed,n))
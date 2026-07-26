class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            heaviest=stones.pop()
            second_heaviest=stones.pop()
            diff=heaviest-second_heaviest
            if diff>0:
                stones.append(diff)
        return stones[0] if stones else 0
stones = [2,7,4,1,8,1]
sol=Solution()
print(sol.lastStoneWeight(stones))
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count=0
        remainders={}
        for t in time:
            r = t % 60 
            complement = (60 - r) % 60
            if complement in remainders:
                count += remainders[complement]
            remainders[r]=remainders.get(r, 0) + 1
        return count
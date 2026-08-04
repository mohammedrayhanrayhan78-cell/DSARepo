class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfied=sum(c for c, g in zip(customers, grumpy) if g == 0)
        extra=0
        for i in range(minutes):
            if grumpy[i]==1:
                extra+=customers[i]
        max_extra=extra
        for i in range(minutes, len(customers)):
            if grumpy[i]==1:
                extra+=customers[i]
            if grumpy[i-minutes]==1:
                extra-=customers[i-minutes]
            max_extra=max(max_extra, extra)
        return base_satisfied + max_extra
class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range (n):
            if(n == 1):
                return True
            if(n == 4):
                return False
            sum=0
            while n>0:
                rem = n%10
                sum=sum+rem*rem
                n//=10
            n= sum
        return n == 1
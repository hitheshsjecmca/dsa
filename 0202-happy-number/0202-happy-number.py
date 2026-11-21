class Solution(object):
    def isHappy(self, n):
        seen=set()

        while n!=1:
            if n in seen:
                return False
            
            seen.add(n)

            t=0
            while n>0:
                d=n%10
                t+=d*d
                n//=10
        
            n=t

        return True
        
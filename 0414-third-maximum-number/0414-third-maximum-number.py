class Solution(object):
    def thirdMax(self, nums):
        l=float('-inf')
        s=float('-inf')
        t=float('-inf')

        for x in nums:
            if x>l:
                t=s
                s=l
                l=x
            elif x>s and x!=l:
                t=s
                s=x
            elif x>t and x!=s and x!=l:
                t=x
        if t==float('-inf'):
            return l
        return t
        
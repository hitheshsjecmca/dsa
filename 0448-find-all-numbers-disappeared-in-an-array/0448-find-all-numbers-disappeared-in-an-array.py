class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        m=[]
        num=set(nums)
        for i in range(1,n+1):
            if i not in num:
                m.append(i)
        return m
        
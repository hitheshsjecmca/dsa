class Solution(object):
    def findDisappearedNumbers(self, nums):

        m=[]
        num=set(nums)

        for i in range(1,len(nums)+1):
            if i not in num:
                m.append(i)
        return m
        
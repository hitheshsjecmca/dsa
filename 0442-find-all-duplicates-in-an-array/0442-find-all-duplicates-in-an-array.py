class Solution(object):
    def findDuplicates(self, nums):
        s=set()
        res=[]

        for x in nums:
            if x in s:
                res.append(x)
            s.add(x)
        return res

        
class Solution(object):
    def findErrorNums(self, nums):
        s=set()

        n=len(nums)

        for x in nums:
            if x in s:
                dup=x
            s.add(x)

        for i in range(1,n+1):
            if i not in nums:
                m=i
        return [dup,m]

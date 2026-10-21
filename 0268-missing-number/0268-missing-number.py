class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        total=0
        ex=n*(n+1)//2
        for x in nums:
            total+=x
        val=ex-total
        return val
        
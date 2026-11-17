class Solution(object):
    def singleNumber(self, nums):

        result=0

        for ch in nums:
            result^=ch
        return result
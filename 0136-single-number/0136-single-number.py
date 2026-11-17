class Solution(object):
    def singleNumber(self, nums):

        freq={}

        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

        for ch in freq:
            if freq[ch]==1:
                return ch
        
class Solution(object):
    def majorityElement(self, nums):
        freq={}

        for x in nums:
            freq[x]=freq.get(x,0)+1
            
            if freq[x] > len(nums)//2:
                return x
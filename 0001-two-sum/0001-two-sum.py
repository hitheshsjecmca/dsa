class Solution(object):
    def twoSum(self, nums, target):
        freq={}

        for i,x in enumerate(nums):
            rem=target-x

            if rem in freq:
                return [freq[rem],i]
            
            freq[x]=i
        
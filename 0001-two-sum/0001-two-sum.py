class Solution(object):
    def twoSum(self, nums, target):
        h={}

        for i,num in enumerate(nums):
            c=target- num

            if c in h:
                return [h[c],i]
            
            h[num]=i
        
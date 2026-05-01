class Solution(object):
    def maxSubArray(self, nums):
        max_=nums[0]
        curr_max=nums[0]

        for i in range(1,len(nums)):
            curr_max=max(nums[i],curr_max + nums[i] )
            max_=max(max_,curr_max)

        return max_

        
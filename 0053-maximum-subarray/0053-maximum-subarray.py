class Solution(object):
    def maxSubArray(self, nums):
        mx=cur=nums[0]
        for x in nums[1:]:
            cur=max(x,x+cur)
            mx=max(mx,cur)
        return mx

        
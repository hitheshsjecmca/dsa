class Solution(object):
    def maxSubArray(self, nums):
        mx=nums[0]
        cur=nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            mx=max(mx,cur)
        return mx

        
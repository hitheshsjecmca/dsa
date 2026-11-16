class Solution(object):
    def maxSubArray(self, nums):

        maximum=nums[0]
        cur=nums[0]

        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            maximum=max(maximum,cur)

        return maximum
        
class Solution(object):
    def minSubArrayLen(self, target, nums):
        ws=0
        l=0
        mn=float('inf')
        for i in range(len(nums)):
            ws+=nums[i]

            while ws>=target:
                mn=min(mn,i-l+1)
                ws-=nums[l]
                l+=1
        if mn==float('inf'):
            return 0
        return mn
                
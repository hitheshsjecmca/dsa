class Solution(object):
    def minSubArrayLen(self, target, nums):
        w_s=0
        l=0
        ml=float('inf')
        for i in range(len(nums)):
            w_s+=nums[i]

            while w_s>=target:
                ml=min(ml,i-l+1)
                w_s-=nums[l]
                l+=1
        if ml==float('inf'):
            return 0
        return ml

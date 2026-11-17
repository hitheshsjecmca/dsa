class Solution(object):
    def maxProduct(self, nums):
        cur_max=nums[0]
        cur_min=nums[0]
        best=nums[0]

        for x in nums[1:]:
            a=cur_max*x
            b=cur_min*x
            cur_max=max(x,a,b)
            cur_min=min(x,a,b)
            best=max(cur_max,best)
        return best        
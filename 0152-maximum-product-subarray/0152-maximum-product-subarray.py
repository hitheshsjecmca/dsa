class Solution(object):
    def maxProduct(self, nums):
        cur_max=nums[0]
        cur_min=nums[0]
        best=nums[0]

        for x in nums[1:]:
            a=cur_max * x
            b=cur_min*x
            cur_max=max(a,b,x) 
            cur_min=min(a,b,x)

            best=max(best,cur_max)

        return best       
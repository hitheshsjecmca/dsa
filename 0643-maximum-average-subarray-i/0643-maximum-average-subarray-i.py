class Solution(object):
    def findMaxAverage(self, nums, k):
        w_s=0
        mx=float('-inf')
        for i in range(len(nums)):
            w_s+=nums[i]
            if i>=k-1:
                avg=float(w_s)/k
                mx=max(avg,mx)
                w_s-=nums[i-k+1]
        return mx



        
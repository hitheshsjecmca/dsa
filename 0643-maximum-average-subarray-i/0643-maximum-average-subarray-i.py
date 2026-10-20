class Solution(object):
    def findMaxAverage(self, nums, k):
        ws=0
        mx=float('-inf')
        for i in range(len(nums)):
            ws+=nums[i]
            if i>=k-1:
                avg=float(ws)/k
                mx=max(avg,mx)
                ws-=nums[i-k+1]
        return mx



        
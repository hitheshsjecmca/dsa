class Solution(object):
    def findKthLargest(self, nums, k):
        
        n=len(nums)
        nums.sort()
        kth=nums[n-k]
        return kth
        
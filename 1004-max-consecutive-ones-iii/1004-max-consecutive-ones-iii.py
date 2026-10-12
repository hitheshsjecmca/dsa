class Solution(object):
    def longestOnes(self, nums, k):
        mx=0
        l=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            while c>k:
                if nums[l]==0:
                    c-=1
                l+=1
            mx=max(mx,i-l+1)
        return mx
        
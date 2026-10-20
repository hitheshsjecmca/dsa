class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        answer=[1]*n

        l=1
        for i in range(n):
            answer[i]=l
            l*=nums[i]

        r=1
        for i in range(n-1,-1,-1):
            answer[i]*=r
            r*=nums[i]
        return answer
        
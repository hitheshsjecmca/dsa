class Solution(object):
    def jump(self, nums):
        j=0
        crend=0
        frend=0

        for i in range(len(nums)-1):
            frend=max(frend,i+nums[i])

            if i==crend:
                j+=1
                crend=frend
        return j
        
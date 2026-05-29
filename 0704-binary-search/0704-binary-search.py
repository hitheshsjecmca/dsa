class Solution(object):
    def search(self, nums, target):
        l=0
        r=len(nums)-1

        while l<=r:
            m=(r+l)/2

            if nums[m] == target:
                return m
            elif target>nums[m]:
                l=m+ 1
            else:
                r=m - 1
        return -1
        
class Solution(object):
    def searchRange(self, nums, target):
        def first():
            l=0
            r=len(nums)-1
            f=-1
            while l<=r:
                m=(l+r)//2

                if nums[m]==target:
                    f=m
                    r=m-1
                elif target>nums[m]:
                    l=m+1
                else:
                    r=m-1
                
            return f
        def last():
            l=0
            r=len(nums)-1
            la=-1
            while l<=r:
                m=(l+r)//2

                if nums[m]==target:
                    la=m
                    l=m+1

                elif target>nums[m]:
                    l=m+1
                else:
                    r=m-1
            return la
        return[first(),last()]
        
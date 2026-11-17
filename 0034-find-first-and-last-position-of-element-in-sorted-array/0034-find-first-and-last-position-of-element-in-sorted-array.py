class Solution(object):
    def searchRange(self, nums, target):
        def find(gf):
            low=0
            high=len(nums)-1
            answer=-1

            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    answer=mid

                    if gf:
                        high=mid-1
                    else:
                        low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1

            return answer

        return [find(True),find(False)]
        
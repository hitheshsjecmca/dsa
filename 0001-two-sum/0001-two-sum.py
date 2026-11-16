class Solution(object):
    def twoSum(self, nums, target):

        seen={}

        for i in range(len(nums)):
            dif=target-nums[i]

            if dif in seen:
                return [seen[dif],i]
            
            seen[nums[i]]=i
        
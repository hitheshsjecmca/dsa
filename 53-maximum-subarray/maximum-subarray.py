class Solution(object):
    def maxSubArray(self, nums):
        current_max=nums[0]
        max_sum=nums[0]

        for num in nums[1:]:
            current_max=max(num, num + current_max)
            max_sum=max(current_max, max_sum)
        return max_sum


class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum=0
        freq={0:1}
        count=0

        for x in nums:
            prefix_sum+=x
            val=prefix_sum-k

            if val in freq:
                count+=freq[val]

            freq[prefix_sum]=freq.get(prefix_sum,0)+1

        return count
        
        
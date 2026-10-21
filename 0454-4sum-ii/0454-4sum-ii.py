class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        freq={}
        res=0

        for a in nums1:
            for b in nums2:
                total=a+b
                freq[total]=freq.get(total,0)+1

        
        for a in nums3:
            for b in nums4:
                total=a+b
                res+=freq.get(-total,0)
        return res
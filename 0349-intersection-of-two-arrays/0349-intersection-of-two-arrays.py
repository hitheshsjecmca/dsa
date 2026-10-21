class Solution(object):
    def intersection(self, nums1, nums2):
        s=set()
        res=set()
        for x in nums1:
            s.add(x)
        
        for x in nums2:
            if x in s:
                res.add(x)
        
        return list(res)
        
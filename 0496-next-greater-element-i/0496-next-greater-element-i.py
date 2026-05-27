class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        s=[]
        n={}

        for nu in nums2:
            while s and nu>s[-1]:
                sm=s.pop()
                n[sm]=nu
            s.append(nu)
        while s:
            n[s.pop()]=-1
        res=[]

        for num in nums1:
            res.append(n[num])
        return res


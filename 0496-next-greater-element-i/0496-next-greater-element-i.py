class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        ng={}
        for num in nums2:
            while stack and stack[-1]<num:
                smaller=stack.pop()
                ng[smaller]=num
            stack.append(num)
        result=[]
        for num in nums1:
            result.append(ng.get(num,-1))

        return result


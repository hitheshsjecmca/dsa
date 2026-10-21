class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        res=0

        for x in s:
            if x-1 not in s:
                count=1

                while x+count in s:
                    count+=1


                res=max(res,count)
            
        return res
        
        
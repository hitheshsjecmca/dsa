class Solution(object):
    def majorityElement(self, nums):
        c=0
        can=None

        for x in nums:
            if c==0:
                can=x

            if x==can:
                c+=1
            else:
                c-=1

        return can
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        r=[]

        def bk(index,subset):
            r.append(subset[:])

            for i in range(index,len(nums)):
                if i > index and nums[i]==nums[i-1]:
                    continue
                
                subset.append(nums[i])
                bk(i+1,subset)
                subset.pop()

        bk(0,[])
        return r
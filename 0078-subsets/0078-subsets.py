class Solution(object):
    def subsets(self, nums):
        r=[]

        def dfs(index,subset):
            if index==len(nums):
                r.append(subset[:])
                return

            subset.append(nums[index])
            dfs(index+1,subset)

            subset.pop()

            dfs(index+1,subset)
            
        dfs(0,[])
        return r
        
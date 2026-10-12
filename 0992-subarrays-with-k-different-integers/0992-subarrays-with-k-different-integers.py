class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(k):
            c=0
            f={}
            l=0

            for i in range(len(nums)):
                f[nums[i]]=f.get(nums[i],0)+1

                while len(f)>k:
                    f[nums[l]]-=1
                    if f[nums[l]]==0:
                        del f[nums[l]]
                    l+=1
                c+=i-l+1
            return c
        return atmost(k)-atmost(k-1)
        
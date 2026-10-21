class Solution(object):
    def findPairs(self, nums, k):
        if k<0:
            return 0

        freq={}

        for x in nums:
            freq[x]=freq.get(x,0)+1

        count=0

        for x in freq:
            if k==0:
                if freq[x]>1:
                    count+=1
            else:
                if x+k in freq:
                    count+=1
        return count
        
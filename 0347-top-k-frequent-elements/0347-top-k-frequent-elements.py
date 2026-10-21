class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}

        for x in nums:
            freq[x]=freq.get(x,0)+1
        
        idea=sorted(freq,key=freq.get,reverse=True)

        return idea[:k]

        
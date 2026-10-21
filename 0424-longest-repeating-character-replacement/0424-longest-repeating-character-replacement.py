class Solution(object):
    def characterReplacement(self, s, k):

        frq={}
        res=0
        mxfq=0
        l=0

        for i in range(len(s)):
            frq[s[i]]=frq.get(s[i],0)+1

            mxfq=max(mxfq,frq[s[i]])

            while (i-l+1)-mxfq>k:
                frq[s[l]]-=1
                l+=1
            
            res=max(res,i-l+1)
        return res

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []

        freq={}
        win={}

        for i in range(len(p)):
            freq[p[i]]=freq.get(p[i],0)+1
        
        res=[]
        k=len(p)

        left=0

        for i in range(len(s)):
            win[s[i]]=win.get(s[i],0)+1

            if i>=k:
                win[s[left]]-=1

                if win[s[left]]==0:
                    del win[s[left]]
                left+=1
            if win==freq:
                res.append(i-k+1)
        return res


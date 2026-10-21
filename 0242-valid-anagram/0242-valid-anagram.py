class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False

        c={}

        for ch in s:
            if ch in c:
                c[ch]+=1
            else:
                c[ch]=1
        
        for ch in t:
            if ch in c:
                c[ch]-=1
            else:
                c[ch]=-1

        for ch in c:
            if c[ch]!=0:
                return False

        return True
        
            
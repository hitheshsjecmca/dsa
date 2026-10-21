class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        c={}

        for cha in s:
            c[cha]=c.get(cha,0)+1
        
        for ch in t:
            if ch not in c:
                return False
            c[ch] -=1

            if c[ch]<0:
                return False
        return True
        
class Solution(object):
    def isAnagram(self, s, t):

        if len(s)!=len(t):
            return False

        count={}

        for ch in s:
            count[ch]=count.get(ch,0)+1

        for a in t:
            if a not in count or count[a]==0:
                return False
            count[a]-=1

        return True

        
class Solution(object):
    def isSubsequence(self, s, t):
        a=0

        for i in range(len(t)):
            if a<len(s) and s[a]==t[i]:
                a+=1

        return a == len(s)
        
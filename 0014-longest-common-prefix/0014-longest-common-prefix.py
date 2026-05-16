class Solution(object):
    def longestCommonPrefix(self, strs):
        p=strs[0]

        for w in strs:
            while w[:len(p)]!=p:
                p=p[:-1]
        return p
        
        
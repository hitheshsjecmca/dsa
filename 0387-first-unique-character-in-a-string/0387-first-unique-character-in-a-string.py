class Solution(object):
    def firstUniqChar(self, s):

        freq={}

        for x in s:
            freq[x]=freq.get(x,0)+1

        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
        
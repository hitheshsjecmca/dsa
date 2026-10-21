class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        freq={}

        for x in magazine:
            freq[x]=freq.get(x,0)+1

        for x in ransomNote:
            if x not in freq or freq[x]==0:
                return False
            freq[x]-=1
        return True
        
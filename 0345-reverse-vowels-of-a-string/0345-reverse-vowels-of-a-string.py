class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        v="aeiouAEIOU"

        l=0
        h=len(s)-1

        while l<h:
            if s[l] not in v:
                l+=1
            elif s[h] not in v:
                h-=1
            else:
                s[l],s[h]=s[h],s[l]
                l+=1
                h-=1

        return"".join(s)       
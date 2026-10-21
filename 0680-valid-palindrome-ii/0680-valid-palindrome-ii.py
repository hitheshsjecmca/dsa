class Solution(object):
    def validPalindrome(self, s):
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return self.checkpalin(s,l+1,r) or self.checkpalin(s,l,r-1)

            l+=1
            r-=1
        return True

    def checkpalin(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1
        return True 
        
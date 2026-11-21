class Solution(object):
    def repeatedSubstringPattern(self, s):
        n=len(s)

        for i in xrange(1,n//2+1):
            if n%i==0:
                sub=s[:i]

                if sub * (n//i)==s:
                    return True
        return False
        
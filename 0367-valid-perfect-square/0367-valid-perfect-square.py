class Solution(object):
    def isPerfectSquare(self, num):

        for i in xrange(1,num+1):
            if i*i==num:
                return True
            if i*i>num:
                return False
        return False
        
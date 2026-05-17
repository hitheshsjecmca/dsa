class Solution(object):
    def compress(self, chars):
        w=0
        l=0

        for r in range(len(chars)):
            if r==len(chars)-1 or chars[r]!=chars[r+1]:
                chars[w]=chars[l]
                w+=1
                c= r - l+1

                if c>1:
                    for d in str(c):
                        chars[w]=d
                        w+=1
                l=r+1
        return w

        
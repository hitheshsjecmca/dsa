from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        need=Counter(t)
        window={}
        have=0
        hc=len(need)
        res=[-1,-1]
        rc=float('inf')

        left=0

        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char,0)+1

            if char in need and window[char]==need[char]:
                have+=1

            while have==hc:
                if (right-left+1)<rc:
                    res=[left,right]
                    rc=right-left+1
                window[s[left]]-=1

                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        left,right=res
        return s[left:right+1] if rc!=float('inf') else ""
        
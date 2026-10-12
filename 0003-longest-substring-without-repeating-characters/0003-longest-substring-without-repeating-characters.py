class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mx=0
        f={}
        l=0

        for i in range(len(s)):
            f[s[i]]=f.get(s[i],0)+1

            while f[s[i]]>1:
                f[s[l]]-=1

                if f[s[l]]==0:
                    del f[s[l]]
                l+=1
            mx=max(i-l+1,mx)
        return mx
        
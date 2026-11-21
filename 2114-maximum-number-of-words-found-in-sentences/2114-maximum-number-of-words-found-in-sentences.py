class Solution(object):
    def mostWordsFound(self, sentences):
        ans=0

        for s in sentences:
            count=len(s.split())
            ans=max(count,ans)

        return ans
        
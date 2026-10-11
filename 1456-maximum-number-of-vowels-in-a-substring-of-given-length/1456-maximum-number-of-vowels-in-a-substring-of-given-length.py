class Solution(object):
    def maxVowels(self, s, k):
        vowels='aeiou'
        mx=0
        c=0

        for i in range(len(s)):
            if s[i] in vowels:
                c+=1
            if i>=k-1:
                mx=max(mx,c)

                if s[i-k+1] in vowels:
                    c-=1
        return mx
        
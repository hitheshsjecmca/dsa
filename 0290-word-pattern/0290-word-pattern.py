class Solution(object):
    def wordPattern(self, pattern, s):

        word=s.split()

        if len(pattern)!=len(word):
            return False

        a={}
        b={}

        for i in range(len(pattern)):
            if word[i] in a and a[word[i]]!=pattern[i]:
                return False
            if pattern[i] in b and b[pattern[i]]!=word[i]:
                return False
            
            a[word[i]]=pattern[i]
            b[pattern[i]]=word[i]

        return True
        
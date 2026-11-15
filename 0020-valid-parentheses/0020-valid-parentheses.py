class Solution(object):
    def isValid(self, s):

        st=[]

        pair={')':'(','}':'{',']':'['}

        for ch in s:
            if ch in '{[(':
                st.append(ch)
            else:
                if not st or st[-1]!=pair[ch]:
                    return False
                
                st.pop()
        return len(st)==0
        
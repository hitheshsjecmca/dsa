class Solution(object):
    def isValid(self, s):
        st=[]
        pair={')':'(','}':'{',']':'['}
        for c in s:
            if c in '[{(':
                st.append(c)
            else:
                if not st or st[-1]!=pair[c]:
                    return False
                st.pop()
        return len(st)==0

                
        
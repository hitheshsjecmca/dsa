class Solution(object):
    def longestValidParentheses(self, s):
        st=[-1]
        mx=0

        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    length=i-st[-1]
                    mx=max(mx,length)
        return mx
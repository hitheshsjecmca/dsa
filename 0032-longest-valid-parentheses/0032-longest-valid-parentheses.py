class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        mx=0

        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    lent=i-stack[-1]
                    mx=max(lent,mx)
        return mx
        
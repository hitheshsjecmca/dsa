class Solution(object):
    def minRemoveToMakeValid(self, s):
        st=[]
        rem=set()

        for i,ch in enumerate(s):
            if ch=='(':
                st.append(i)
            elif ch==')':
                if st:
                    st.pop()
                else:
                    rem.add(i)
        while st:
            rem.add(st.pop())
        res=[]

        for i,ch in enumerate(s):
            if i not in rem:
                res.append(ch)
        return "".join(res)
                
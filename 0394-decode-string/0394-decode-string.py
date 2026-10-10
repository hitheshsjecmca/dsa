class Solution(object):
    def decodeString(self, s):
        sc=[]
        nc=[]
        number=0
        cur=""
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch == "[":
                sc.append(cur)
                nc.append(number)
                number=0
                cur=""
            elif ch=="]":
                count=nc.pop()
                prev=sc.pop()
                cur=prev+cur*count
            else:
                cur+=ch
        return cur        
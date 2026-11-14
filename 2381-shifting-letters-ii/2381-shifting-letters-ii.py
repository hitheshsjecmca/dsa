class Solution(object):
    def shiftingLetters(self, s, shifts):

        n=len(s)

        arr=[0]*(n+1)

        for start,end,direction in shifts:
            if direction==1:
                val=+1
            else:
                val=-1

            arr[start]+=val
            arr[end+1]-=val

        
        cur=0
        res=[]
        for i in range(n):
            cur+=arr[i]

            ch=(ord(s[i])-ord('a') +cur)%26
            res.append(chr(ch+ord('a')))

        return "".join(res)
        
class Solution(object):
    def divisorSubstrings(self, num, k):
        x=str(num)
        count=0
        for i in range(len(x)-k+1):
            sub=int(x[i:i+k])

            if sub != 0 and num % sub==0:
                count+=1
        return count


        
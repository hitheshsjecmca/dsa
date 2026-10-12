class Solution(object):
    def totalFruit(self, fruits):
        mx=0
        f={}
        l=0

        for i in range(len(fruits)):
            f[fruits[i]]=f.get(fruits[i],0)+1

            while len(f)>2:
                f[fruits[l]]-=1
                if f[fruits[l]]==0:
                    del f[fruits[l]]
                l+=1
            mx=max(i-l+1,mx)
        return mx
        
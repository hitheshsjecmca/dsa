class Solution(object):
    def dailyTemperatures(self, temperatures):
        res=[0]*len(temperatures)
        s=[]

        for i, t in enumerate(temperatures):
            while s and t> temperatures[s[-1]]:
                p=s.pop()
                res[p]=i-p

            s.append(i)

        return res
        
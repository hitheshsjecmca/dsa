class Solution(object):
    def maximumPopulation(self, logs):

        arr=[0]*101

        for birth,death in logs:
            arr[birth-1950]+=1
            arr[death-1950]-=1

        cur=0
        max_pop=0
        ans=1950

        for i in range(101):
            cur+=arr[i]

            if cur>max_pop:
                max_pop=cur
                ans=i+1950

        return ans
        
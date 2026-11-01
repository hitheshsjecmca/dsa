class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        start=0
        tank=0
        total=0

        for i in range(len(gas)):
            diff=gas[i]-cost[i]

            total+=diff
            tank+=diff

            if tank<0:
                start=i+1
                tank=0

        if total<0:
            return -1

        return start
        
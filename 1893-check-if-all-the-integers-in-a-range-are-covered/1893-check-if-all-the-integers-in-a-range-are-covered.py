class Solution(object):
    def isCovered(self, ranges, left, right):
        arr=[0]*52

        for start,end in ranges:
            arr[start]+=1
            arr[end+1]-=1

        cur=0

        for i in range(52):
            cur+=arr[i]

            if left<=i<=right:
                if cur==0:
                    return False
        return True
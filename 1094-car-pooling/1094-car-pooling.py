class Solution(object):
    def carPooling(self, trips, capacity):
        arr=[0]*1001

        for pas,start,end in trips:
            arr[start]+=pas
            arr[end]-=pas

        current=0
        for i in arr:
            current+=i

            if current>capacity:
                return False
        
        return True
        
class Solution(object):
    def corpFlightBookings(self, bookings, n):

        arr=[0]*(n+1)

        for first,last,seats in bookings:
            arr[first-1]+=seats
            arr[last]-=seats

        cur=0
        res=[]

        for i in range(n):
            cur+=arr[i]
            res.append(cur)

        return res
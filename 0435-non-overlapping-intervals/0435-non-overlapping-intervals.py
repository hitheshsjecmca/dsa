class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])

        rem=0
        prevend=intervals[0][1]

        for i in range(1,len(intervals)):

            if intervals[i][0]<prevend:
                rem+=1
            else:
                prevend=intervals[i][1]
        return rem
        
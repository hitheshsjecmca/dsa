class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        max_width=0
        while l < r:
            h = min(height[l],height[r])
            width=r-l
            max_width=max(max_width,h*width)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return max_width

        
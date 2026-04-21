class Solution(object):
    def sortedSquares(self, nums):
        squares=[]
        for x in nums:
            squares.append(x*x)
        squares.sort()
        return squares
        
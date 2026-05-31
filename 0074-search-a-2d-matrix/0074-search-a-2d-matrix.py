class Solution(object):
    def searchMatrix(self, matrix, target):
        row=len(matrix)
        cols=len(matrix[0])

        l=0
        ri=row * cols -1
         
        while l<=ri:
            m=(l+ri)//2

            r=m//cols
            c=m%cols

            value=matrix[r][c]

            if value== target:
                return True
            elif value < target:
                l=m+1
            else:
                ri=m-1
        return False

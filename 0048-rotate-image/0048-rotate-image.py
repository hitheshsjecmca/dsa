class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
           l=0
           r=n-1

           while l<r:
            row[l],row[r]=row[r],row[l]
            l+=1
            r-=1
        
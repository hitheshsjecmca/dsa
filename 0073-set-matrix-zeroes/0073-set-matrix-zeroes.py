class Solution(object):
    def setZeroes(self, matrix):

        m=len(matrix)
        n=len(matrix[0])

        zr=[]
        zc=[]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zr.append(i)
                    zc.append(j)


        for i in zr:
            for j in range(n):
                matrix[i][j]=0

        for i in zc:
            for j in range(m):
                matrix[j][i]=0

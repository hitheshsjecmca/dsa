class Solution(object):
    def solveNQueens(self, n):
        result=[]

        cols=set()
        d1=set()
        d2=set()

        board=[["."]* n for _ in range(n)]

        def backtrack(row):

            if row==n:
                copy=["".join(r) for r in board]
                result.append(copy)
                return
            for col in range(n):
                if ( 
                    col in cols or
                    (row-col) in d1 or
                    (row+col) in d2
                ): 
                    continue
            
                cols.add(col)
                d1.add(row-col)
                d2.add(row+col)

                board[row][col]="Q"

                backtrack(row+1)

                board[row][col]="."

                cols.remove(col)
                d1.remove(row-col)
                d2.remove(row+col)


        backtrack(0)
        return result
        
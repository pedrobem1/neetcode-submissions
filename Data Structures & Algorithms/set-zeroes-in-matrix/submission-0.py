class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        col_zeros = set()
        row_zeros = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zeros.add(row)
                    col_zeros.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in row_zeros:
                    matrix[row][col] = 0

                if col in col_zeros:
                    matrix[row][col] = 0          




                if row in row_zeros:
                    matrix[row][col] = 0

                if col in col_zeros:
                    matrix[row][col] = 0

                

    
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        rows_up = 0
        rows_down = rows - 1
        selected_row = rows_down

        while rows_up <= rows_down:
            rows_mid = (rows_up + rows_down) // 2
            if target < matrix[rows_mid][0]:
                rows_down = rows_mid - 1
            elif target > matrix[rows_mid][cols-1]:
                rows_up = rows_mid + 1
            else:
                selected_row = rows_mid
                break
           
        cols_left = 0
        cols_right = cols - 1
        while cols_left <= cols_right:
            cols_mid = (cols_left + cols_right) // 2
            if target < matrix[selected_row][cols_mid]:
                cols_right = cols_mid - 1
            elif target > matrix[selected_row][cols_mid]:
                cols_left = cols_mid + 1
            else:
                return True
        return False

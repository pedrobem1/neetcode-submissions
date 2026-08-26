class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # 1. Binary search para encontrar a linha
        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1

            elif target > matrix[mid][-1]:
                top = mid + 1

            else:
                # target está dentro do intervalo dessa linha
                row = mid
                break
        else:
            return False

        # 2. Binary search dentro da linha
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif target < matrix[row][mid]:
                right = mid - 1

            else:
                left = mid + 1

        return False

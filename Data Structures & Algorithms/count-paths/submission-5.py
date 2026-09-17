class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row == m-1 or col == n-1:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row+1][col] + grid[row][col+1]

        return grid[0][0]

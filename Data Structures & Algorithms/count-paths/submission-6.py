class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * n
        
        for row in range(m-2,-1,-1):
            for col in range(n-1,-1,-1):
                if col == n-1:
                    grid[col] = 1
                else:
                    grid[col] = grid[col] + grid[col+1]

        return grid[0]

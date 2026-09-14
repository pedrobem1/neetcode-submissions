class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def dfs(row, col):
        #     if (row,col) in memo:
        #         return memo[(row,col)]
        #     if row >= m or col >= n:
        #         return 0

        #     if row == m-1 and col == n-1:
        #         return 1

        #     down = dfs(row + 1, col)
        #     right = dfs(row, col + 1)

        #     memo[(row,col)] = down + right
        #     return (memo[(row,col)])

        # return dfs(0,0)

        memo = [[0] * n for _ in range(m)]
        memo[m-1][n-1] = 1
        

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m-1 or j == n-1:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i+1][j] + memo[i][j+1]


        return memo[0][0]



            
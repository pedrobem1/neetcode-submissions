class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        islands = 0

        def bfs(row,col):
            q = collections.deque()

            q.append((row,col))

            while q:
                qLen = len(q)
                for i in range (qLen):
                    row,col = q.popleft()
                    for dr,dc in directions:
                        r, c = row + dr, col + dc
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                            grid[r][c] = "3"
                            q.append((r,c))

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = "3"
                    islands += 1
                    bfs(row,col)

        return islands

        

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        healthy = 0
        q = collections.deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    healthy += 1

        minutes = 0

        while q:
            qLen = len(q)
            for i in range(qLen):
               row, col = q.popleft()
               for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        healthy -= 1
                        q.append((r,c))

            minutes += 1

        if healthy == 0:
            return max(minutes-1,0)

        return -1


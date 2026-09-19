class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        max_area = 0

        def bfs(row, col) -> int:
            q = collections.deque()
            q.append((row,col))
            size = 1
            while q:
                qLen = len(q)
                for i in range(qLen):
                    row,col = q.popleft()
                    for dr,dc in directions:
                        r,c = row + dr, col + dc
                        if 0 <= r < rows and 0 <= c < cols and (r,c) not in seen and grid[r][c] == 1:
                            seen.add((r,c))
                            q.append((r,c))
                            size += 1
            return size


        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in seen:
                    seen.add((row,col))
                    area = bfs(row,col)
                    max_area = max(max_area, area)



        return max_area
            
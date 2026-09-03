class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c) -> int:
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            cur_area = 1

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
                        cur_area += 1
            return cur_area

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    cur_area = bfs(r, c)
                    max_area = max(max_area, cur_area)

        return max_area

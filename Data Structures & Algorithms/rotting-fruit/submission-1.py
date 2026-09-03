class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        

        visit = set()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    fresh += 1
                elif grid[r][c] == 2 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r, c))

        
        minutes = 0
        while q and fresh > 0:
            qLen = len(q)
            for _ in range(qLen):
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == 1:
                        q.append((r,c))
                        fresh -= 1
                        visit.add((r,c))
            minutes += 1
        
        if fresh != 0:
            return -1

        return minutes

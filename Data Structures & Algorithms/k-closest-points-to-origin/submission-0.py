import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x1, y1 = point[0],point[1]
            x2, y2 = 0, 0
            dist = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            distances.append((dist, x1, y1))

        minHeap = distances
        heapq.heapify(minHeap)
        res = []
        count = 0
        while count < k:
            p = heapq.heappop(minHeap)
            res.append((p[1],p[2]))
            count += 1

        return res

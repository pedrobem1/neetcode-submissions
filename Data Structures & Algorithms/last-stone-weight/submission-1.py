import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = stones
        for i in range(len(minHeap)):
            minHeap[i] = -minHeap[i]
        heapq.heapify(minHeap)

        #[2,3,6,2,4] -> [-2,-3,-6,-2,-4] -> [-6,-4,-2,-3,-2] (minHeap)
        while len(minHeap) > 1:
            x =  - heapq.heappop(minHeap) # biggest
            y = - heapq.heappop(minHeap) # second biggest

            if x > y: # x > y
                x -= y
                heapq.heappush(minHeap,-x)
        if minHeap:
            return -minHeap[0]

        return 0


            

            

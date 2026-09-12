class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        count = 0
        element = 0
        while count < k:
            element = - heapq.heappop(maxHeap)
            count += 1
            
        return element
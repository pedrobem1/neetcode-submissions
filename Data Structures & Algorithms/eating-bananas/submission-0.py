class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        limit = 0
        for pile in piles:
            if pile > limit:
                limit = pile
        left = 1
        right = limit
        lowest_k = limit
        while left <= right:
            k = (left+right) // 2
            hours= 0

            for pile in piles:
                if pile <= k:
                    hours += 1
                else:
                    hours += -(pile // -k) #-(a // -b) -> funcao teto
            if hours <= h: # este valor de k deu certo
                right = k - 1
                lowest_k = k
            else: # hours > h
                left = k + 1
        
        return lowest_k



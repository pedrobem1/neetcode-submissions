class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(index):
            if index in cache:
                return cache[index]

            if index >= len(cost):
                return 0
            
            one_step = dfs(index+1)
            two_step = dfs(index+2)
            cache[index] = cost[index] + min(one_step, two_step)

            return cache[index]

        return min(dfs(0),dfs(1))
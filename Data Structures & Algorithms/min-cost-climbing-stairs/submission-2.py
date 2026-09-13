class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Minimum cost to reach the previous step and the step before that
        step1 = 0
        step2 = 0

        for i in range(2, len(cost) + 1):
            # Cost to reach this current step
            current_step = min(step1 + cost[i - 1], step2 + cost[i - 2])

            step2 = step1
            step1 = current_step

        return step1
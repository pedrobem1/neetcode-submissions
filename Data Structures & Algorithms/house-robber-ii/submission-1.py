class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_simple(houses) -> int:
            cache = {}
            def dfs(index):
                if index in cache:
                    return cache[index]
                if index >= len(houses):
                    return 0

                rob = dfs(index+2)
                not_rob = dfs(index+1)
                
                cache[index] = max(houses[index] + rob, not_rob)

                return cache[index]
            return dfs(0)

        return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))
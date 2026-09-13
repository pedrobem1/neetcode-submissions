class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(index):
            if index in cache:
                return cache[index]
            if index >= len(nums):
                return 0

            rob = dfs(index+2)
            not_rob = dfs(index+1)
            
            cache[index] = max(nums[index] + rob, not_rob)

            return cache[index]

        return dfs(0)
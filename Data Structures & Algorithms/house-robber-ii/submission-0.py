class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        cache = {}
        def dfs(index):
            if index in cache:
                return cache[index]
            if index >= len(nums)-1:
                return 0

            rob = dfs(index+2)
            not_rob = dfs(index+1)
            
            cache[index] = max(nums[index] + rob, not_rob)

            return cache[index]
        
        cache2 = {}
        def dfs2(index):
            if index in cache2:
                return cache2[index]
            if index >= len(nums):
                return 0

            rob = dfs2(index+2)
            not_rob = dfs2(index+1)
            
            cache2[index] = max(nums[index] + rob, not_rob)

            return cache2[index]


        return max(dfs(0),dfs2(1))
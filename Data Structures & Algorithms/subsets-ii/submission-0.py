class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort() # So all the duplicates are next to each other

        def backtracking(n):
            if n == len(nums):
                res.append(path[:])
                return

            path.append(nums[n]) # Subsets that include nums[n]
            backtracking(n+1)
            path.pop()
            
            # Subsets that dont include nums[n]
            while n + 1 < len(nums) and nums[n] == nums[n+1]:
                n += 1
            backtracking(n+1)

        backtracking(0)
        return res
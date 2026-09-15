class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(n):
            if n == len(nums):
                res.append(path[:])
                return

            path.append(nums[n])
            backtracking(n+1)
            path.pop()
            backtracking(n+1)

        backtracking(0)
        return res


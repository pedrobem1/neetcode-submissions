class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking():
            if len(path) == len(nums):
                res.append(path[:])

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtracking()
                path.pop()

        backtracking()
        return res
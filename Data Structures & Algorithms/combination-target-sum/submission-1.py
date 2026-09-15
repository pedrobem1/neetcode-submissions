class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        summ = 0
        def backtracking(n,summ):
            if n == len(nums) or summ > target:
                if summ == target:
                    res.append(path[:])
                return
            
            path.append(nums[n])
            backtracking(n, summ + nums[n])
            path.pop()
            backtracking(n+1,summ)


        backtracking(0,summ)
        return res
            
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        curr_cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_cons += 1
                max_cons = max(max_cons,curr_cons)
            else:
                curr_cons = 0

        return max_cons
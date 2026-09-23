class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_lenght = float('inf')
        curr_sum = 0
        for right, num in enumerate(nums):
            curr_sum += num

            
            while left <= right and curr_sum >= target:
                min_lenght = min(min_lenght, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
        if min_lenght == float('inf'):
            return 0
        return min_lenght
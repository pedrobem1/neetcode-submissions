class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        if len(nums) == 0:
            return 0
            
        seen = set()

        for i in range(len(nums)):
                seen.add(nums[i])
            
        if len(seen) == 1:
            return 1

        for i in range(len(nums)):
            curr = 1
            k = 1
            if i-1 >= 0 and (nums[i] - 1) in seen: # nums[i] does not start a sequence
                continue
            while (nums[i] + k) in seen:
                curr += 1
                longest = max(longest, curr)
                k += 1

        return longest
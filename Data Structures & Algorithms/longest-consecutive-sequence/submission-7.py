class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0


        seen = set(nums)
            

        for num in seen:
            if (num-1) not in seen:
                lenght = 1
                while (num + lenght) in seen:
                    lenght += 1
                longest = max(longest, lenght)
                

        return longest
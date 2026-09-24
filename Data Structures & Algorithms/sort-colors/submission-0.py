class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        frequencies = {0: 0, 1: 0, 2: 0}
        for num in nums:
            frequencies[num] += 1

        zero_freq = frequencies[0]
        one_freq = frequencies[1]
        two_freq = frequencies[2]

        for i in range(0, zero_freq):
            nums[i] = 0

        for i in range(zero_freq, zero_freq + one_freq):
            nums[i] = 1

        for i in range(zero_freq + one_freq, len(nums)):
            nums[i] = 2

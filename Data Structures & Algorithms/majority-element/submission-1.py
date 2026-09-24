class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = {}

        for i in range(len(nums)):
            if nums[i] not in frequencies:
                frequencies[nums[i]] = 1
            else:
                frequencies[nums[i]] += 1

        maj_freq = float('-inf')
        maj_elem = float('-inf')

        for ele, freq in frequencies.items():
            if freq > maj_freq:
                maj_freq = freq
                maj_ele = ele


        return maj_ele
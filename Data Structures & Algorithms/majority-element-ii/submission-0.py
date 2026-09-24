class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        count1 = 0
        cand2 = None
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == cand1:
                count1 += 1
            elif nums[i] == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = nums[i]
                count1 = 1
            elif count2 == 0:
                cand2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        threshold = len(nums) // 3

        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                res.append(cand)

        return res
            
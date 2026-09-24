class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid-1]:
                if mid - 1 >= 0 and (mid-1) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
            elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                if (mid) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return nums[mid]
        if len(nums) == 1:
            return nums[0]
        return -1
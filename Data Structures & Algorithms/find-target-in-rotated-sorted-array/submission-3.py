class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        # min in the array
        while left < right:
            mid = (left+right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid 
            
        # left tem o indice do menor elemento
        pivot = left

        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid -1 
            else:
                left = mid + 1

        return -1





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        # nums[j] + nums[k] = - nums[i]
        #-> target = -nums[i]
    
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1 
            
            target = -nums[index]
            while left < right:
                current = nums[left] + nums[right]
                if current == target:
                    if [nums[index],nums[left],nums[right]] not in triplets:
                        triplets.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif current < target:
                    left += 1
                else:
                    right -= 1
        return triplets
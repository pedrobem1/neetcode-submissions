class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums=[1,1,1,2,2,3]
        count = 1
        index = 1
        i = 0
        current_int = nums[0]
        while index < len(nums):
            if nums[index] != current_int:
                if count >= 2:
                    nums[i] = current_int
                    nums[i+1] = current_int
                    i += 2
                else:
                    nums[i] = current_int
                    i += 1

                count = 1
                current_int = nums[index]
                index += 1
                
            
            else:
                count += 1
                index += 1
            
            if index == len(nums):
                    if count >= 2:
                        nums[i] = current_int
                        nums[i+1] = current_int
                        i += 2
                    else:
                        nums[i] = current_int
                        i += 1

        return i
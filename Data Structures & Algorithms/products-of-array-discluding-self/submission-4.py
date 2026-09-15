class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        output = [0] * len(nums)
        count_zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_zeros += 1
            else:
                mul *= nums[i]
        
        for i in range(len(nums)):
            if count_zeros == 0:
                output[i] = mul // nums[i]
            elif count_zeros >= 2:
                output[i] = 0
            else: # Only 1 zero
                if nums[i] == 0:
                    output[i] = mul
                else:
                    output[i] = 0

        return output




        
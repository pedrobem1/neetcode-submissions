class Solution:
    def check(self, nums: List[int]) -> bool:
        #count quedas incluindo de nums[-1] para nums[0]
        count = 0
        for i in range(0,len(nums)-1):
            if nums[i+1] < nums[i]:
                count +=1

        if nums[-1] > nums[0]:
            count +=1

        return (count <= 1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        pos = 0
        for i in nums:
            complemento = target - i
            
            if complemento in hashmap:
                return [hashmap[complemento], pos]

            if i not in hashmap:
                hashmap[i] = pos
            

            pos += 1
        return []
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        freq2 = {}
        

        for i in range(len(nums1)):
            if nums1[i] in freq1:
                freq1[nums1[i]] += 1
            else:
                freq1[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in freq2:
                freq2[nums2[i]] += 1
            else:
                freq2[nums2[i]] = 1

        ans = []
        for num in freq1:
            if num in freq2:
                ans.append(num)

        return ans
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n2 = len(nums2)

        k = m
        for i in range(n2):
            nums1[k] = nums2[i]
            k += 1

        nums1.sort()
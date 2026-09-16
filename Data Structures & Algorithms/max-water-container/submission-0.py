class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxx = 0

        for i in range(len(heights)):
            if left == right:
                break
            area = (right-left) * min(heights[left],heights[right])
            maxx = max(maxx,area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxx
            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxx = 0
        left = 0

        for right, char in enumerate(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            
            curr = right - left + 1
            maxx = max(maxx,curr)

        return maxx
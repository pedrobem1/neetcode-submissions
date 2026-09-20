class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        seen = {} #s[letter]: last_index
        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)

            seen[s[right]] = right
            curr = right - left + 1
            longest_sub = max(longest_sub, curr)

        return longest_sub  
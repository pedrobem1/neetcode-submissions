class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0 
        left = 0
        for right,char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            current = right - left + 1

            if current > longest:
                longest = current
        
        return longest
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        max_freq = 0
        left = 0
        max_lenght = 0

        for right,char in enumerate(s):
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1 
            
            max_freq = max(max_freq,frequencies[char])

            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1 

            current = right - left + 1
            max_lenght = max(current, max_lenght)

        return max_lenght


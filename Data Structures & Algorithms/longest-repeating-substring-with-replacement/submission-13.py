class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}

        maxx = 0
        left = 0
        for right, char in enumerate(s):
            if char not in frequencies:
                frequencies[char] = 1
            else:
                frequencies[char] += 1

            curr = right - left + 1 # Len da janela
            max_char = max(frequencies.values())
            while curr - max_char > k:
                frequencies[s[left]] -= 1
                if frequencies[s[left]] == 0:
                    del frequencies[s[left]]
                left += 1

                curr = right - left + 1 # Len da janela
                max_char = max(frequencies.values())

            maxx = max(maxx, right - left + 1)
        
        return maxx

            
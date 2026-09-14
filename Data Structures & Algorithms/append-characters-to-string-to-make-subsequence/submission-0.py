class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j >= len(t):
                break
            if s[i] == t[j]:
                i += 1
                j += 1
            
            


        return len(t) - j

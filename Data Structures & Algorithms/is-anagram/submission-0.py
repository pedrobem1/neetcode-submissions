class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        
        for i, letter in enumerate(s):
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
            
        for letter in t:
            if letter in count:
                count[letter] -= 1
            else: 
                return False
            
        for i in count:
            if count[i] != 0:
                return False
        return True




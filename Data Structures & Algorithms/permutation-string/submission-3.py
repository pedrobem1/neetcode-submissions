class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap c/ window (de tamanho len(s1))
        hashmap1 = {}
        for l in s1:
            if l not in hashmap1:
                hashmap1[l] = 1
            else:
                hashmap1[l] += 1
        hashmap2 = {}
        left = 0
        for right, letter in enumerate(s2):
            if letter in hashmap2:
                hashmap2[letter] += 1
            else:
                hashmap2[letter] = 1

            if right - left == len(s1):
                hashmap2[s2[left]] -= 1
                if hashmap2[s2[left]] == 0:
                    del hashmap2[s2[left]]
                left += 1 
            
            if hashmap1 == hashmap2:
                    return True
        
        return False
            

                


            
            
            
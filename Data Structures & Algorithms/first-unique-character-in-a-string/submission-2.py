class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] = -1
            else:
                hashmap[s[i]] = i 
            

    
    

        minn = len(s)
        for key in hashmap:
            if hashmap[key] < minn and hashmap[key] != -1:
                minn = hashmap[key]
        if minn == len(s):
            return -1
        return minn


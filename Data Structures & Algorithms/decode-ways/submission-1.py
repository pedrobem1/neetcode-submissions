class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(index):
            if index in cache:
                return cache[index]
            if index >= len(s):
                return 1
            if s[index] == "0":
                return 0

            single = dfs(index + 1)
            if index+1 < len(s) and (int(s[index]) == 1 or (int(s[index]) == 2 and int(s[index+1]) <= 6)):
                double = dfs(index + 2)
            else:
                double = 0

            cache[index] = single + double
            return (single + double)

        if s[0] == "0":
            return 0
        return(dfs(0))

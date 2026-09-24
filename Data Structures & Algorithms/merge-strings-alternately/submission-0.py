class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) + len(word2)
        new_str = ''

        for index in range(n):
            if index >= len(word1) or index >= len(word2):
                break
            new_str = new_str + word1[index]
            new_str = new_str + word2[index]

        if len(word1) > len(word2):
            new_str = new_str + word1[index:]

        elif len(word1) < len(word2):
            new_str = new_str + word2[index:]

        return new_str

            
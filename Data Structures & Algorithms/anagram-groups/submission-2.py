class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else:
                hashmap[sorted_word].append(word)

        res = []
        for key, values in hashmap.items():
            res.append(values)

        return res


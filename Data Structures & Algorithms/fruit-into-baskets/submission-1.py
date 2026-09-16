class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        frequencies = {} 
        maxx = 0
        left =  0

        for right, fruit in enumerate(fruits):
            if fruit not in frequencies:
                frequencies[fruit] = 1
            else:
                frequencies[fruit] += 1

            while len(frequencies) > 2:
                frequencies[fruits[left]] -= 1
                if frequencies[fruits[left]] == 0:
                    del frequencies[fruits[left]]
                left += 1

            curr = right - left + 1
            maxx = max(maxx,curr)

            
        return maxx
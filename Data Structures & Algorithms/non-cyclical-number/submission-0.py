class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.replace(n)
            if n == 1:
                return True


        return False


    def replace(self, n) -> int:
        summ = 0
        for char in str(abs(n)):
            digit = int(char)
            summ += digit * digit

        return summ
            
        
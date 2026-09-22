class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0
        str_num = str(x)
        right = len(str_num) - 1

        while left < right:
            if str_num[left] != str_num[right]:
                return False
            left += 1
            right -= 1

        if len(str_num) == 1:
            if x < 0 :
                return False
            
        return True

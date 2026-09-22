from functools import cmp_to_key


class Solution:

    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(num) for num in nums]

        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1  # x deve vir antes de y
            elif x + y < y + x:
                return 1  # y deve vir antes de x
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))

        result = "".join(nums_str)

        return "0" if result[0] == "0" else result
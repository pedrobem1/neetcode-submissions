class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        if len(s) == 1 or not s:
            return False

        stack = []

        for char in s:
            if char in ['(','[','{']:
                stack.append(pairs[char])

            else:
                if len(stack) > 0:
                    complement = stack.pop()
                    if char == complement:
                        continue
                    else:
                        return False
                return False

        if len(stack) == 0:
            return True
        return False
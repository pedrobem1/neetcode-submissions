class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        if len(s) == 0:
            return True

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) > 0:
                    if (stack[-1] == pairs[char]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
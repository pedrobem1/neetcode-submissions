class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        index = 0
        while index < len(s):
            if s[index] is not "]":
                stack.append(s[index])

            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string

                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                k = int(k)
                stack.append(string * k)

            index += 1

        return "".join(stack)

                    
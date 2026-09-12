class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Add elements to stack until a symbol. Then, remove the last 2 elements from the stack, perform the operation and add the result back on the stack

        stack = [] # 10 6 9 3 +
        for element in tokens:
            if element not in ["+","-","*","/"]:
                stack.append(int(element))

            else:
                if element == "+":
                    x1 = int(stack.pop())
                    x2 = int(stack.pop())
                    stack.append(x1 + x2)

                elif element == "-":
                    x1 = int(stack.pop())
                    x2 = int(stack.pop())
                    stack.append(x2 - x1)

                elif element == "*":
                    x1 = int(stack.pop())
                    x2 = int(stack.pop())
                    stack.append(x1 * x2)

                elif element == "/":
                    x1 = int(stack.pop())
                    x2 = int(stack.pop())
                    stack.append(int(x2 / x1))
        
        return stack[0]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            elif asteroids[i] < 0:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
                while len(stack) > 0 and -asteroids[i] >= stack[-1]:
                    if stack[-1] < 0:
                        break
                        
                    if -asteroids[i] == stack[-1]:
                        stack.pop()
                        break

                    stack.pop()

                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(asteroids[i])

        return stack
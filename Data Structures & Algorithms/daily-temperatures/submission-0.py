class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack [(38,1) ,  ]
        # output [1-0 , 0 , 0 , 0 , 0 , 0 , 0]

        stack = []
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, index))

            else:
                while temp > stack[-1][0]:
                    last_element = stack.pop()
                    output[last_element[1]] = index - last_element[1]
                    if len(stack) == 0:
                        break
                stack.append((temp, index))
                
            
                
            
        return output

                
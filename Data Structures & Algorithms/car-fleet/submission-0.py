class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True) 
        stack = []

        for index, car in enumerate(pos_speed):
            if len(stack) == 0:
                stack.append(car)
            else:
                last_car = stack[-1]
                last_car_time = (target - last_car[0]) / last_car[1]
                cur_car_time = (target - car[0]) / car[1]

                stack.append(car)
                if cur_car_time <= last_car_time:
                    stack.pop()

        return len(stack)


             



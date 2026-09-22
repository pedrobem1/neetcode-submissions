class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        index = 0

        while index < len(intervals):
            new_interval = intervals[index]

            while index+1 < len(intervals) and intervals[index+1][0] <= new_interval[1]:
                new_limit = max(new_interval[1], intervals[index+1][1])
                new_interval = [new_interval[0],new_limit]
                index += 1

            answer.append(new_interval)
            index += 1

        return answer
        

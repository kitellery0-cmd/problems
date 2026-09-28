class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]: # interval is after
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: # interval is before
                res.append(newInterval)
                res.extend(intervals[i : ])
                return res
            else: # overlap. merge needed
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end] # merge
        res.append(newInterval) # interval is at end
        return res

# start by sorting the intervals by their start time 
# note: do not look at approach #1 using graph, it is uncessarily complicated 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # when the end of current interval >= the start of next interval, then there is an overlap 
        def sort_func(x): 
            return x[0]
        intervals.sort(key=sort_func)
        merged = []

        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                # when the merged list is empty, or when the end of previous interval < start of current interval 
                # this means the current interval doesn't have overlap so far and should be added to merged
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        return merged
# sol 1: use a min heap to store the ending time of meeting rooms 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        import heapq
        if not intervals: 
            return 0 
        
        intervals.sort(key=lambda x: x[0]) # sort intervals by start time 
        heap = []

        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i][0]:
                # when heap is not empty and min end time <= start time of current meeting
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)



# sol 2: chronological ordering 
# note: I find the loop logic in the offcial Leetcode solution 
# is confusing, follow what I write below. 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # first, get two arrays "start" and "end", each sorted by time
        start = [i[0] for i in intervals]
        start.sort()
        end = [i[1] for i in intervals]
        end.sort()

        room_required = 0
        end_idx = 0

        for start_idx in range(len(start)):
            if start[start_idx] < end[end_idx]: 
                # if start time is less than end time, we need a new room
                room_required += 1 
            else: 
                # otherwise, we keep min number of required room constant
                # and move the end_idx to next end time.
                # this represents that the current meeting 
                # takes an available room that is already allocated 
                end_idx += 1
            
        return room_required 

# my sol, not correct! 
# 54/79 test cases passed, 
# failed test case: [[9,10],[4,9],[4,17]] -> should be 2 meeting room required instead of 3
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by start time to find overlapping intervals 
        intervals.sort(key=lambda x: x[0])
        print("intervals after sort: {}".format(intervals))

        max_room_count = 1 # at least 1 meeting room is needed since intervals can not be empty

        
        i = 1
        current_interval = intervals[0]
        while i < len(intervals):
            
            current_room_count = 1
            while i < len(intervals) and intervals[i][0] < intervals[i-1][1]:
                # there is an overlap 
                current_room_count += 1
                print("at index {}, current_room_count: {}".format(i, current_room_count))
                current_interval[0] = intervals[i][0] # update start time of overlap 
                current_interval[1] = min(intervals[i-1][1], intervals[i][1]) # update end time of overlap 
                i += 1
                if current_room_count > max_room_count: 
                    max_room_count = current_room_count
                
            if i < len(intervals): 
                current_interval = intervals[i]
                i+=1
            
        return max_room_count





# sol 1: use a min heap to store the end time of events 
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq
        max_day = max([event[1] for event in events])
        events.sort() #sort by start time 
        heap = []
        event_count = 0
        event_idx = 0

        for current_day in range(1, max_day + 1): 
            while event_idx < len(events) and events[event_idx][0] <= current_day: 
                # add events that is already started 
                heapq.heappush(heap, events[event_idx][1])
                # note here we increase event_idx, so that we only 
                # go through the events list ONCE for the entier for loop
                event_idx += 1
            
            while heap and heap[0] < current_day: 
                # remove events that already ended 
                # note the top of heap is the min end time 
                heapq.heappop(heap)
            
            if heap:
                # there's at least 1 event we can attend! Attend the one with min end time 
                heapq.heappop(heap)
                event_count += 1
        
        return event_count
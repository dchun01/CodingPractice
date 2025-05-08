class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda interval: interval[1])
        def overlap(interval1, interval2):
            return (interval1[0] < interval2[1] and interval1[1] > interval2[0]) or (interval1[0] == interval2[0] and interval1[1] == interval2[1])
        i = 0
        while i < len(intervals):
            if i == len(intervals)-1:
                return True
            interval = intervals[i]
            interval2 = intervals[i+1]
            if overlap(interval, interval2):
                return False
            i += 1

        return True

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # no overlap
                merged.append(interval)
            else:   # overlap
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
# code
dfs
```py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def dfs(i, prev):
            if i == len(intervals):
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res

        return len(intervals) - dfs(0, -1)
```

sorting sol
```py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]
        
        return res
```

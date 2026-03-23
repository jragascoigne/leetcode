# intuition
note it tles on leetcode..

# code
```py
class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = {}
        if timestamp not in self.d[key]:
            self.d[key][timestamp] = []
        self.d[key][timestamp].append(value)

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        seen = 0

        for time in self.d[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        return "" if seen == 0 else self.d[key][seen][-1]        

```

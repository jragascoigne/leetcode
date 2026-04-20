# code
naive solution
```py
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_d = 0
        for i, c1 in enumerate(colors):
            for j, c2 in enumerate(colors):
                if c1 != c2:
                    max_d = max(max_d, abs(i - j))
        
        return max_d
```

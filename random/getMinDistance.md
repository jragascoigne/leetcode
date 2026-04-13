# intuition
i started with a naive approach, looping through all the values in the list and comparing them. when i found an index that matched i would store it and continue.
this passed the base cases but when there were multiple of the same value it would end up being the wrong distance in some cases. after thinking about the approach
a bit, i realised we dont need to store the index at all, we just want the minimum distance, so we can iterate over the list and as we go pick out the min distance
if the numbers match. for most cases this only happens once, however for cases where there are multiple of the smae value in the list this comparison happens n times.

# code
```py
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m_d = 100000
        for i, n in enumerate(nums):
            if n == target:
                m_d = min(m_d, abs(i - start))
        
        return m_d

```

# intuition
initial sol - sort and return nums[-k] lol. however this is obv not what is wanted.
i had to think of a way to solve this question without sorting
i landed on the suggested heapq solution, heapq.nlargest

# code
```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

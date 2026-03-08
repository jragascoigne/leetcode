# code
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        count = sum(nums[:k])
        max_val = count

        for r in range(k, len(nums)):
            count += nums[r]
            count -= nums[r - k]
            max_val = max(max_val, count)
        
        return max_val / k
```

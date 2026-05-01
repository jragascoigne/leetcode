# code
```py
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        f = sum(i * nums[i] for i in range(n))
        max_val = f
        
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            max_val = max(max_val, f)
        
        return max_val
```

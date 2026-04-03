# code
naive
```py
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        
        return res

```

sliding window
```py
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for i, r in enumerate(nums):
            if r == 0:
                l = i + 1
            else:
                res = max(res, i - l + 1)

        return res
```

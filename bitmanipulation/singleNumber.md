# code
```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                s.remove(n)
        
        return s.pop()

```

bit manupulation sol
```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res
```

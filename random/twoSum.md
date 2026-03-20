# code
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []

        for i in range(len(nums) - 1):
            r = len(nums) - 1

            while r > i:
                if nums[i] + nums[r] == target:
                    return [i, r]
                else:
                    r -= 1
```

        
# hash map sol (beats 100%)
``` py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            
            d[n] = i
        
        return []
```

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

        

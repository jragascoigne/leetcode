# code
```py
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        cur_max = 0

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            cur_max = max(cur_max, right - left + 1)

        return cur_max
```

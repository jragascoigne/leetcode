# code
```py
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        if len(nums) != mx + 1:
            return False

        freq = [0] * (mx + 1)

        for x in nums:
            if x < 1 or x > mx:
                return False

            freq[x] += 1

        for i in range(1, mx):
            if freq[i] != 1:
                return False

        return freq[mx] == 2
```

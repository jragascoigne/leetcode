# intuition
after watching the neetcode video it made sense that this was a sequence question. need to go back and do these 1d-dp q's again

# code
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            one = one + two
            two = one - two
        
        return one
```

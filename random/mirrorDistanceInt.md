# intuition
i wrote this in about a minute, and tried to get it down to as few lines as possible. actually while im writing this i can see how to make it one line
# code
```py
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return(abs(n - int("".join(reversed(str(n))))))
```

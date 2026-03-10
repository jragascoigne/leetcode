# code
```py
class Solution:
    def myAtoi(self, s: str) -> int:
        LB = -(2**31)
        UB = (2**31) - 1
        s = s.lstrip()

        if not s:
            return 0

        positive = True
        if s[0] in '+-':
            positive = s[0] == '+'
            s = s[1:]

        digits = ''
        for c in s:
            if c.isdigit():
                digits += c
            else:
                break

        if not digits:
            return 0

        result = int(digits)
        if not positive:
            result = -result

        return max(LB, min(UB, result))
```

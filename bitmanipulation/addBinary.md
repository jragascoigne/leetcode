# code
```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        c = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or c:
            if i >= 0:
                c += int(a[i])
                i -= 1
            
            if j >= 0:
                c += int(b[j])
                j -= 1

            s.append(str(c % 2))
            c //= 2
        
        return ''.join(reversed(s))

```

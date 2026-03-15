# intuition
i knew that updating list for each mult/addition would tle, but i didnt think about how we could get around this.
storing the mult and add as two values and applying them at the getIndex method was genius, but it was also still hard for me to
figure out what the question was asking me for that method.

# code
```py
MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.raw = []
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv = pow(self.mult, MOD-2, MOD)
        base = (val - self.add) * inv % MOD
        self.raw.append(base)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mult = self.mult * m % MOD
        self.add = self.add * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.raw):
            return -1
        return (self.raw[idx] * self.mult + self.add) % MOD
```

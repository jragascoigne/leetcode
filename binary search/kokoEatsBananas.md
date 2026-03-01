# intuition
one thing that always catches me out for koko is that we are running binary search on the k value, not the piles themselves. it seems obvious in retrospect but given the question i always default to running it on the piles.

writing a loop function helps with passing in an m value

# code
class Solution:
    def loop(self, piles: List[int], h: int, k: int) -> int:
        total = 0
        for i in range(len(piles)):
            total += math.ceil(float(piles[i]) / k)
        
        return (total <= h)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        tot = r

        while l <= r:
            m = l + ((r-l) // 2)

            if self.loop(piles, h, m):
                r = m - 1
                tot = m
            
            else:
                l = m + 1
        
        return tot
        
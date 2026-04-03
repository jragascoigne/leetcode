# intuition
o(n2) sol. we are sorting at every step here, but it's necessary as we always want to pick the two biggest stones.
at every step in the while loop, the two biggest stones n[-2] and n[-1] are selected and hit together.
if they are equal to one another, both are popped, otherwise one is popped and the other has its
value set to the difference between the two stones (with abs).
then just return the value of the final stone if the length of stones is [greater than 0] equal to 1
else 0. 

# code
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-2]
            y = stones[-1]

            if x == y:
                stones.pop()
                stones.pop()
            
            else:
                stones.pop()
                stones[-1] = abs(y - x)
            
        return stones[0] if len(stones) == 1 else 0
```

heap sol
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
```

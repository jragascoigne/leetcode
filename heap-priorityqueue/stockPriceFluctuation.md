# intuition
initially, a stack with tuples (index, value). however i decided to use a dict to store indexes and values.
then my solution TLE'd on the max and min methods, so i had to use min and max heaps for those methods instead.

# code
```py
from collections import defaultdict
import heapq

class StockPrice:

    def __init__(self):
        self.prices = defaultdict(int)
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        while -self.max_heap[0][0] != self.prices[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap[0][0] != self.prices[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
```

# intuition
just looked at the neetcode video and need to go over this one because it feels like a huge step up from prev problems.

# code
```py
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
```

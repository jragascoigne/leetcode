# intuition
this is a naive solution, the time complexity is terrible and its on the slowest side on leetcode. however, i couldnt think of another way to do it?
my first thought would be a different data structure, potentially a hash map so we can index in o[1] time. this solution works by adding and then only performing
a sort when we go to find the median, so i think its o[n] where n is the size of the datastream.

# code
```py
class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        odd = (len(self.data) % 2 != 0)

        if odd:
            middle = len(self.data) // 2
            return float(self.data[middle])
        
        else:
            m1 = len(self.data) // 2 - 1
            m2 = m1 + 1
            mean = (self.data[m1] + self.data[m2]) / 2
            return float(mean)
```
        
        

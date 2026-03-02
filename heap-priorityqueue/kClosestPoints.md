# intuition
initially i was using a dictionary to map all the values to the POINT INDEXES in the dict, so that i could then use a lambda
function to sort the values and return the k indexed point tuples as a list of points. however this solution is a little more efficient
as i am just sorting the points by their distances and then appending them to a new list. 

# code
```py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s_d = sorted(points, key=lambda item: ((item[0])**2 + (item[1])**2) ** 0.5)
        
        ret = []
        for i in range(k):
            ret.append(s_d[i])

        return ret
```

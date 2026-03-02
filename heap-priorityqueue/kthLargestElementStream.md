# intuition
we need to define k and the array in the constructor using the passed in values, so...
then, when add is called we want to sort the array after the value has been added and return the kth largest
value

we can do this simply by returning (len arr - k) which gives the index of the kth largest element (as we have already sorted!)

# code
```py
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
```

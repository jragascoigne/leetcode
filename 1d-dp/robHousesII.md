# intuition
the intuition with this q is to reuse house rob 1, and we have to call this function more than once.
we need to convert this to a helper function and return the max of the two function calls, one where we skip the first house
and one where we skip the last house.

we also return the max of nums[0] as well if it's bigger than the other two, as in this case this handles the base case of len(nums) == 1.

# code
```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
```

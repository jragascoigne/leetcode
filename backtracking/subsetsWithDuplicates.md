# intuition
i used my intital subsets solution and thought to apply the logic from combinationsum2, where i skip over duplicated elements that have already been added 
in the 'left hand side'. these will still be considered but duplicates will be negated

# code
```py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
```

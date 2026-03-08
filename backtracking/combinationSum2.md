# intuition
i thought i was being lazy by copying in the solution from combination sum 1 after reading the question...
i knew the pop and dfs on i+1 logic were to skip a number in the list so i applied this to the first dfs call.
this was getting the right numbers but out of order, so i sorted it at the top.
now i was just getting duplicates of every substring but they were correct. i thought it had to be the wrong approach,
so i watched the video and he did the same as me just with incrementing i if the next num is equal to the cur num.
this means that all of the numbers will get used recursively but no more at the OTHER step, so 'all' of them are exclusive to
one solution at one step.


# code
```py
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur, total + nums[i])
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, cur, total)        
        dfs(0, [], 0)
        return res
```

# intuition
reading the problem, we know that temperature days increase every time until there is a number larger than itself. so, when the incoming t value is larger than the top value in the stack, we want to pop that value off, as well as any values in the stack that meet those requirements. we can use the difference between the current i value and the i value we're passing into the stack to find the value for us to append to the result

# code
```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = (i - stack_i)

            stack.append([t, i])
        
        return res
```

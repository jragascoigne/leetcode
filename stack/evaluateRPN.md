# intuition
this problem becomes a lot easier when you break it into 'cases', where you consider each operator to be its own case.
stack is the most optimal data structure here as RPN takes from the most recent first.

# code
```py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())

            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b / a)))
            
            else:
                stack.append(int(t))
        
        return stack[0]
```

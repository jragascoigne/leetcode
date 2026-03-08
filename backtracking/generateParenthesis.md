# code
```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
    
        def dfs(cur, copen, cclose):
            if copen > n or cclose > copen:
                return
            
            if copen == n == cclose:
                res.append("".join(cur))
                return

            if copen < n:
                cur.append('(') 
                dfs(cur, copen + 1, cclose)
                cur.pop()
            if cclose < copen:
                cur.append(')')
                dfs(cur, copen, cclose + 1)
                cur.pop()
        
        dfs([], 0, 0)
        return res
```

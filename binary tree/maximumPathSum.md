# code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        def dfs(root):
            nonlocal max_val
            if not root:
                return

            left = self.get_max(root.left)
            right = self.get_max(root.right)
            
            max_val = max(max_val, root.val + left + right)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return max_val
        
    def get_max(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.get_max(root.left)
        right = self.get_max(root.right)
        path = root.val + max(left, right)
        return max(0, path)   

```


# revised solution
more time efficient, did away with the helper function.

```py

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')

        def dfs(root):
            
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.max_val = max(self.max_val, root.val + left + right)

            return root.val + max(left, right)
    
        dfs(root)
        return self.max_val

```

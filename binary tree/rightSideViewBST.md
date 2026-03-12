# intuition
note: this solution only works on BSTS, as they have to be in order ( w max on the right, min on the left)
this is because im grabbing the max at every depth, otherwise i'm not sure how to do this

# code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        return [max(res[j]) for j in range(len(res))]
```

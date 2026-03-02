# intuition
i thought about max depth and thought of DFS, and recursive dfs was the simple solution so I went with it. next time I solve i will try a different method and put it here

# code

# recursive dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        

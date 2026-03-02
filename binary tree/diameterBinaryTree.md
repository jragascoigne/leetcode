# intuition
i knew initially that something with dfs would be involved. i had to watch the video explaination on this problem, but as i understand it:
at every dfs step we are setting the result to the larger of either the result or the diameter at the dfs step. we are returning in the dfs loop
the longest length of left and right and adding the root node to it (+1).

we then just need to call dfs on the root and return the result.

# code

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1
        
        dfs(root)
        return self.res


        

# intuition
a balanced binary tree is that all subtrees differ in height by no more than one. so, at every DFS step, if the result of left or right is greater than the
other by more than 1, the tree is considered unbalanced.
WE ARE RETURNING -1 IF LEFT OR RIGHT DOESNT EXIST AND ALSO IF THE DIFFERENCE IS GREATER THAN 1.

# code
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1: return -1

            right = dfs(node.right)
            if right == -1: return -1

            if abs (left - right) > 1:
                return -1

            return 1 + max(left, right)

            
        return dfs(root) != -1
            

        

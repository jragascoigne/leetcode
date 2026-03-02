# intuition
check if p and q are null, if they both are this is considered the same tree (edge case)
otherwise at every step if p and q and their values match, they are considered the same tree.
IF the values match but they are out of place this is considered two separate trees which this handles automatically!

# code
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False        

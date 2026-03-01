# 23. Merge k Sorted Lists

# intuition
i thought back to the merge 2 linked lists solution i had done, and how it could be applied to K lists. i realised that K lists is really just 2 lists, k-1 times. so i pulled my 2 list solution in and then used a for loop, for i in range(1, k) and merged lists i and i-1. then i returned lists[-1] (or lists[0])
though this isnt the most efficient solution, i can't think of a better way to do it.

# code
<!-- # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next -->
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next  
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
            return dummy.next
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])
        
        if not lists:
            return None
            
        return lists[-1]
        
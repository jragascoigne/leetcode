# 19 - Remove Nth Node From End of List (med)

# intuition
my initial idea was to use a dummy list and a while loop. this mostly worked
but some edge cases were incorrect. after watching neetcode's video, i understood
that i wanted to use 2p with a dummy list.

v         v      
1 -> 2 -> 3 -> 4 -> 5 ->(null)

so, if n = 2, right pointer is l + n away from left pointer. this means that when the right pointer
reaches the end (null), the left pointer will be in the right spot to perform 'deletion'
which is setting left.next to left.next.next

          v
1 -> 2 -> 3 -> 4 -> 5 

becomes 1 -> 2 ----> 4 -> 5



# code
<!-- 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next -->

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        t = ListNode(0, head)
        left = t
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return t.next
        

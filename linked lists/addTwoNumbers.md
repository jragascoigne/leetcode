# 2. Add Two Numbers (med)

# intuition

initial approach was to get l1 and l2 nexts, add their values and set a cur dummy next to the result
i failed to consider the proper way to do this with cur.next = ListNode(val) where val is l1.val + l2.val.

consulting the neetcode sol, its similar to mine but with the carry involved. i knew at some point i was going to have to work this part out but using mods and division for the place indicators
is a robust approach. in retrospect i realise this problem is all about the thought process and understanding how to implement moreso than any complex algorithm, which i touched on in another sol.

# code
<!-- # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next -->

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0

        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
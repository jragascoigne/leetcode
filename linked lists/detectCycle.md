# 141. Linked List Cycle (easy)

# intuition
this was pretty easy to understand coming off the floyd's problem which utilized this slow and fast pointer logic. i knew i needed two pointers, one going twice as fast through the list. i thought that at any point if slow == fast then return true, where slow and fast are initialized both as head but iterate before being checked.

while fast (ie while head), and while there is a non null value being pointed to in fast, we increase slow by one and fast by two. if the lists are equal then we can return true, but if fast reaches the end and is set to null, we return false

# code
<!-- # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next -->

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        
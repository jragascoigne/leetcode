# 138. Copy List with Random Pointer (med)

# intuition

initial idea, i had no clue how to approach this problem. as the question asks for a deep copy of the list i imagined making a new list and for each index, the Node.random pointer would be set to Node.(next) * i for each Node.

after watching neetcode solution, it made more sense to use a hashmap as it meant every node could be stored for the second iteration of the loop. from my understanding, the value of the nodes is the random pointer, so by saving the cur node's key as cur and the value as the random pointer it's easily accessed afterwards.

i'm starting to understand that these linked list questions are a lot more intuition based and less about algorithms.

# code
<!-- """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
""" -->

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None : None }

        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]

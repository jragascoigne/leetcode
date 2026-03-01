# 287. find the duplicate number

# intuition
initial naive solution thoughts were use a hash map and use 2p, of which i wrote both of these solutions out. i feel like i must be missing the idea or concept behind this, so i'll watch the video on it and see what he has to say.

so the example uses floyd's algorithm and two pointers - slow and fast to find cycles like in previous questions. again, the code itself is simple but the logic and understanding is complex.

# code

# naive 1 - hash map
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                return n

this uses o(n) extra space which the question asks for o(1), so invalid.

# naive 2 - 2p O(n2)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums):
            for r in range(l+1, len(nums)):
                if nums[l] == nums[r]:
                    return nums[r]
            
            l += 1

uses o(1) extra space as everything is done in place, however inefficient o(n2) time complexity.

# sol - floyd's (2p)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
                
        

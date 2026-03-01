# 704. binary search (easy)

# intuition:
basic binary search implementation. __ONE THING TO NOTE:__ m = (l + r) // 2 can lead to overflow, so remember to make sure to do m = l + ((r-l) // 2) to avoid and prevent this
another thing that caught me up this time was the while loop being l <= r, where i forgot to do the equals. quickly sorted this tho.

# code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-l) // 2)
            
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        
        return -1

        
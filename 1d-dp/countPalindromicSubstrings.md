# intuition
i used my palindromic substring code from the other solution and changed the logic. its useful to be able to reuse code where possible but it would 
have been beneficial for me to write it from scratch again. the main difference was appending all palindromes to a list and returning the length of this
list as the count. in this case, instead of checking the length and seeing if its greater than our current max, we append ALL substrings regardless
of if they're duplicates (ie, 'aa' 'aa' at different indexes).

# code
```py
class Solution:
    def countSubstrings(self, s: str) -> int:

        palindromes = []

        for i in range(len(s)):
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes.append(s[l:r+1])
                
                l -= 1
                r += 1
            
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes.append(s[l:r+1])
                
                l -= 1
                r += 1
        
        return len(palindromes)
```

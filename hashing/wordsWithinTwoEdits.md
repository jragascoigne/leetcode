# code
```py
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # for l in words
        # for word in dictionary
        # if diff in words < 2 add to ret list
        # else forget abt it 

        res = []

        def get_distance(s1, s2):
            c = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    c += 1
                if c == 3:
                    return False
            return True

        for query in queries:
            for d in dictionary:
                dist = get_distance(query, d)
                if dist:
                    res.append(query)
                    break
        
        return res
```

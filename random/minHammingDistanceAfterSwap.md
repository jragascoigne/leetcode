# code
```py
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i,j in allowedSwaps:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        def dfs(node,comp):
            if node in visited:
                return
            visited.add(node)
            comp.append(node)
            for i in graph[node]:
                dfs(i,comp)
        res=0
        for i in range (len(source)):
            if i not in visited:
                component=[]
                dfs(i,component)
                src_cnt=Counter(source[idx] for idx in component)
                for f in component:
                    if src_cnt[target[f]]>0:
                        src_cnt[target[f]]-=1
                    else:
                        res+=1
        return res
```

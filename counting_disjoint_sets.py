from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in edges:
            union(u, v)
        
        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1
        return count

n = 5
edges = [[0,1],[1,2],[3,4]]
print(countComponents(n, edges))
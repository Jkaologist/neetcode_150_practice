class UnionFindByrank:
    def __init__(self):
        self.roots = self.ranks = []
    def union_find(self, size):
        self.roots = self.ranks = [0] * size
        for i in range(size):
            self.roots[i] = self.ranks[i] = i
    def test_union_find(self):
        self.union_find(5)
        print(union_finder.roots, union_finder.ranks)
    def find(self, x):
        while x != self.roots[x]:
            self.roots[x] = self.roots[self.roots[x]]
            x = self.roots[x]
        return x
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.ranks[root_x] > self.ranks[root_y]:
                self.roots[root_y] = root_x
            elif self.ranks[root_y] > self.ranks[root_x]:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x
                self.ranks[root_x] += 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


union_finder = UnionFindByrank()
# Test Case
union_finder.union_find(10)
# 1-2-5-6-7 3-8-9 4
union_finder.union(1, 2)
union_finder.union(2, 5)
union_finder.union(5, 6)
union_finder.union(6, 7)
union_finder.union(3, 8)
union_finder.union(8, 9)
print(union_finder.is_connected(1, 5))  # true
print(union_finder.is_connected(5, 7))  # true
print(union_finder.is_connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
union_finder.union(9, 4)
print(union_finder.is_connected(4, 9))  # true

union_finder.test_union_find() # prints roots and ranks lists for size 5

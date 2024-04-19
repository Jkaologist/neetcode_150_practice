import itertools

a = [1,2,3]
b = ["a", "b", "c"]

permutations = itertools.permutations(a)
for g in list(permutations):
    print(*g, sep=' ')

permutations = itertools.permutations(b, 2)
for g in list(permutations):
    print(*g, sep=' ')
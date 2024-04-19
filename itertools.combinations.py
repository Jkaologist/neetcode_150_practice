import itertools

a = [1,2,3]
b = ["a", "b", "c"]

# All combinations without repeat values
combinations = itertools.combinations(range(4), 3)
for g in list(combinations):
    print(*g, sep=' ')

combinations = itertools.combinations(b, 2)
for g in list(combinations):
    print(*g, sep=' ')

# Combinations with repeated values
combinations = itertools.combinations_with_replacement(a, 3)
for g in list(combinations):
    print(*g, sep=' ')
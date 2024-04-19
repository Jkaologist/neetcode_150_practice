import itertools

l = range(100)

filtered = itertools.filterfalse(lambda n: n % 2 == 0, l)
print(list(filtered))

filtered = itertools.filterfalse(lambda n: n % 2 == 1, l)
print(list(filtered))

l = [0, 1, False, True]
filtered = itertools.filterfalse(None, l)
print(list(filtered))
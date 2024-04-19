import itertools

l = ["a", "b", "c", "a", "b", "c"]
sliced = itertools.islice(l, 2)
print(list(sliced))
import itertools

a = [1,2,3]
b = ["a", "b", "c"]
c = [True, True, False]
combined = itertools.chain(a, b, c)
print(list(combined))
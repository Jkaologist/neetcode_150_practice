from itertools import product

# help(product)
prod = product('ab', range(3))
print(list(prod))
print(prod)
for i in product('ab', range(3)):
    print(i)

prod = product((0, 1), (0, 1), (0, 1))
print(list(prod))
for i in product((0, 1), (0, 1), (0, 1)):
    print(i)

a = [1,2,3]
b = ["a", "b", "c"]

out = product(a, b, repeat=2) # cartesian products
for t in out:
    print(t)
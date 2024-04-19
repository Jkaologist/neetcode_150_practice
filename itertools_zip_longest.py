import itertools

a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,8]
c = [1,2,3,4,5,6,7,8]
d = [True, "a"]
# Exhausts at longest element
zipped = itertools.zip_longest(a, b, c, d, fillvalue=None) # AKA zipped = itertools.zip_longest(a, b, c, d)
print(list(zipped))
zipped = itertools.zip_longest(a, b, c, d, fillvalue="FILLED")
print(list(zipped))
# Exhausts at shortest element
z = zip(a, b, c, d)
print(list(z))
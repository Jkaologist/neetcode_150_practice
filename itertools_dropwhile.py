import itertools

l = [1,2,3,4,5,6,7,1,1,2]

remaining = itertools.dropwhile(lambda n: n < 3, l)
print(list(remaining))
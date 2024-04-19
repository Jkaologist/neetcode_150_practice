import itertools

l = [1,2,3,4,5,6,7,8]
taken = itertools.takewhile(lambda a: a < 4, l)
print(list(taken))
import itertools

s = "abcde"
paired = itertools.pairwise(s)

print(list(paired))
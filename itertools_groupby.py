import itertools

lst = [(c, i) for i, c in enumerate("GKLAAAAQRSAXAAAAYZ")]
print(lst)
grouped = itertools.groupby(lst, lambda key: key[0],)
for key, value in grouped:
    print(key, list(value), sep=": ")

lst = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,2,2,2,2,2,1,1,1,1]
example = [list(g) for k, g in itertools.groupby(lst)]
print(example)

import itertools

l = [1,2,3,"a","b","c",7,8]
tee = itertools.tee(l, 3)
for it in tee:
    print(list(it))

tee = itertools.tee(["123"], 3)
for it in tee:
    print(list(it))
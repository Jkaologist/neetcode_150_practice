def build_lists_of_sets(N):
    cols = list(map(lambda _: set(), ([None] * N)))
    cols_again = [set() for _ in range(N)]
    cols_again_again = []
    for _ in range(N):
        cols_again_again.append(set())

    for c in cols:
        print("memory addresses of exlicit iterator: ", id(c))
    for c in cols_again:
        print("memory addresses of exlicit iterator: ", id(c))
    for c in cols_again_again:
        print("memory addresses of exlicit iterator: ", id(c))
    return cols


lst = [1, 2, 3, 3, 4, 5, 6]
cpy1 = lst[::]
cpy2 = lst.copy()
cpy3 = lst
print(
    "ORIGINAL === ",
    id(lst),
    "\n",
    "DEEP COPY === ",
    id(cpy1),
    "\n",
    "DEEP COPY === ",
    id(cpy2),
    "\n",
    "SHALLOW COPY ===",
    id(cpy3),
)

print(build_lists_of_sets(9))  # True

# generate all possible cascading combinations of a list of numbers

lst = [1,2,3]

def cascade_combinations(lst):
    out = [[]]
    for num in lst:
        out += [current + [num] for current in out]
    return out

print(cascade_combinations(lst))
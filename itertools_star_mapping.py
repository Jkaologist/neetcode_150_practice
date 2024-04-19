import itertools
from operator import pow, add

lst = [(2,3), (2,4), (2,5)]

star_mapped = itertools.starmap(pow, lst)
print(list(star_mapped))
star_mapped = itertools.starmap(add, lst)
print(list(star_mapped))

def add_x_to_args(*args):
    temp = []
    for arg in args:
        temp.append(f"{arg}X")
    return temp

star_mapped = itertools.starmap(add_x_to_args, lst)
print(list(star_mapped))
import itertools

letters = ["a", "b", "c", "d"]
selectors = [True, True, False, True]
compressed = itertools.compress(letters, selectors)
print(list(compressed))
selectors = [1,1,1]
compressed = itertools.compress(letters, selectors)
print(list(compressed))
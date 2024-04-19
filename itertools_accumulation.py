import itertools
import operator

nums = [5,4,3,2,1]

accumulation = itertools.accumulate(nums)
# AKA accumulation = itertools.accumulate(nums, operator.add)
print(list(accumulation))
accumulation = itertools.accumulate(nums, operator.mul)
print(list(accumulation))
accumulation = itertools.accumulate(nums, operator.pow)
print(list(accumulation))
letters = ["A", "B", "CD"]
accumulation = itertools.accumulate(letters, operator.concat)
print(list(accumulation))
lsts = [[123], ["ABC"], [True]]
accumulation = itertools.accumulate(lsts, operator.concat)
print(list(accumulation))




nums = [1,2,2,3,3,3,4,5,5,5,6]

unique_uses_a_lot_of_memory = set([x**2 for x in nums])
unique_fast = set(x**2 for x in nums)
unique_fastest = {x**2 for x in nums}

print(unique_uses_a_lot_of_memory)
print(type(unique_uses_a_lot_of_memory))

print(unique_fast)
print(type(unique_fast))

print(unique_fastest)
print(type(unique_fastest))

s = set()
for num in nums:
    s.add(num**2)
print(s)
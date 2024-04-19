import itertools

counter = itertools.count(10, 2)
for i in counter:
    print(i)
    if i == 20:
        break

l = ["A", "B", "C"]
cycler = itertools.cycle(l)
for i, letter in enumerate(cycler):
    print(i, letter, sep=": ")
    if i == 10:
        break

s = "hello_world"
repeater = itertools.repeat(s, 5)
print(list(repeater))
for s in itertools.repeat(s, 5):
    print(s)
s = "hello world"
iterator = reversed(s)
lst = list(iterator)
s = ""
for c in lst:
    s += c
print(s)
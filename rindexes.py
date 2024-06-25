s = "helloworld"
lookup = {}
for idx, char in enumerate(s):
    lookup[char] = idx

lookup2 = {}
s2 = set(s)
for c in s2:
    # r_idx = s.rindex(c)
    r_idx = s.rfind(c)
    lookup2[c] = r_idx

print(lookup2)

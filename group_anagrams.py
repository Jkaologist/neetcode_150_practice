def group_anagrams(strs):
    anagrams, out = {}, []
    for s in strs:
        key = "".join(sorted(s))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    for anagram in anagrams.values():
        out.append(anagram)
    return out


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))

def is_anagram(s1, s2):
    return s1 == s2[::-1]


print(is_anagram("hello", "world"))
print(is_anagram("level", "level"))

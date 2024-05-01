s = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content,"
s2 = "car ca cab c"

def lexicographic_sort(s):
    words = s.split()
    words.sort()
    return words

print(lexicographic_sort(s))
print(lexicographic_sort(s2))
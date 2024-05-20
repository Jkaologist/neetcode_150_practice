from bisect import bisect, bisect_left
lst = [-1, 3, 18, 150, -5, -50, 0]
lst.sort()
print(lst)
res1 = bisect_left(lst, 3)
res2 = bisect(lst, 3) # AKA bisect_right
print(res1, res2)

def grade(score, breakpoints = [60, 70, 80, 90], grades = "FDCBA"):
    i = bisect(breakpoints, score)
    return grades[i]
grades = [grade(score) for score in [33, 99, 77, 70, 97, 82, 40, 100]]
print(grades)
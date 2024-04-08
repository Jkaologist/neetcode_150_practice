def find_all_combinations(lst = [1,2], target= 4):
    out = []
    def find_combinations(start = 0, end = len(lst), target = target, combination = []):
        if target == 0:
            out.append(combination)
            return
        if target < 0:
            return
        for i in range(start, end):
            find_combinations(i, end, target - lst[i], combination + [lst[i]])
    find_combinations()
    return out

print(find_all_combinations([1,2], 4))
print(find_all_combinations([1,2,3], 4))
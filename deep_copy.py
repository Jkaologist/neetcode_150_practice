import copy

lst = [1,2,3, {"a": 1}]

lst2 = lst[:]
lst3 = copy.copy(lst)
lst4 = list(lst)
lst5 = [i for i in lst]
lst6 = lst * 1
lst7 = lst[::]
lst8 = lst[0:4]
lst9 = lst[0:len(lst)]
lst10 = lst[0:]
lst12 = lst
lst13 = copy.deepcopy(lst)

lst[3]["a"] = "SHALLOW COPY"

print(lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst12, lst13)
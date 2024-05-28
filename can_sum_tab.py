def can_sum(nums, target):
    table = [False] * (target + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in nums:
                if num + i < len(table):
                    print(num + i)
                    table[num + i] = True
    print(table)
    return table[-1]

can_sum([3,4,5,7], 7) # T
# # recursion
# def climbing_stairs(n):
#     memo = {}
#     def climb(num):
#         if num in memo:
#             return memo[num]
#         if num > n:
#             return 0
#         if num == n:
#             return 1
#         memo[num] = climb(num + 1) + climb(num + 2)
#         return memo[num]
#     return climb(0)

# print(climbing_stairs(3))
# print(climbing_stairs(5))
# print(climbing_stairs(9))


# tabulation
def climbing_stairs(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(len(table)):
        print(table)
        if i + 1 < len(table):
            table[i + 1] += table[i]
        if i + 2 < len(table):
            table[i + 2] += table[i]
    return table[n]

print(climbing_stairs(1)) # 1
print(climbing_stairs(2)) # 1
print(climbing_stairs(3)) # 2
print(climbing_stairs(4)) # 3
# print(climbing_stairs(5)) # 5
# print(climbing_stairs(6)) # 8
# print(climbing_stairs(7)) # 13
# print(climbing_stairs(8)) # 21
# print(climbing_stairs(50)) # 12586269025

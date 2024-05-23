# Write fib(n) such that it takes in a number as an argument. 
# The function should return the nth number of the Fibonacci Sequence.

def fib(n):
    table = [0] * (n + 1)
    # each subproblem corresponds to an element in the list
    # fibonacci contributes to the sum of the next two positions
    table[1] = 1
    # for i in range(2, n + 1):
    #     table[i] = table[i- 1] + table[i - 2]
    for i in range(n):
        if i < n - 1:
            table[i + 2] += table[i]
        table[i + 1] += table[i]
    print(table)
    return table[-1]

print(fib(6)) # 8

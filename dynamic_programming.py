memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)
    memo[n] = res
    return res

print(fib(5))
print(fib(50))

def fib_tabular(n):
    memo = {}
    for i in range(1, n + 1):
        if i <= 2:
            res = 1
        else: 
            res = memo[i - 1] + memo[i-2]
        memo[i] = res
        return res

print(fib(5))
print(fib(50))
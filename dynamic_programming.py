def fib(n):
    if n <= 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    return res

print(fib(5))
# you are given a list of coin values
# pick any coins with repeats
# return the minimum amount of coins it would take to make the sum amount
# return -1 if there is no way to make the total amount

from math import inf

# # top down
def coinChange(coins, amount):
    memo = {}
    def top_down(amount, min_count = inf):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0

        for coin in coins:
            rem = amount - coin
            if rem >= 0:
                min_count = min(min_count, 1 + top_down(rem))
        
        memo[amount] = min_count
        return min_count
    return top_down(amount) if top_down(amount) != inf else -1

# # bottom up
# def coinChange(coins, amount):
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#     for coin in coins:
#         for x in range(coin, amount + 1):
#             dp[x] = min(dp[x], dp[x - coin] + 1)
#     return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([1,2], 3))
print(coinChange([3,4], 2))
print(coinChange([1,2,5], 55))

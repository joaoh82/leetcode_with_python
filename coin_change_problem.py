# Given a number of cents in change return the number of coins needed
# to build change
# num_coins(33) -> 1 (25), 1 (5), 3(1)

# Brute forced`
def num_coins(value):
    count = 0
    while value > 0:
        if value // 25 > 0:
            count += value // 25
            value = value % 25
        elif value // 10 > 0:
            count += value // 10
            value = value % 10
        elif value // 5 > 0:
            count += value // 5
            value = value % 5
        elif value // 1 > 0:
            count += value // 1
            value = value % 1
    return count

print(num_coins(33))

# Optimized solution
# time O(1) - number of coins, so constant
def num_coins_optimized(value):
    num_of_coins = 0
    coins = [25, 10, 5, 1]
    while value > 0:
        for coin in coins:
            if value // coin > 0:
                num_of_coins += value // coin
                value = value % coin
    return num_of_coins

print(num_coins_optimized(33))
print(num_coins_optimized(0))
print(num_coins_optimized(1))
print(num_coins_optimized(5))
print(num_coins_optimized(26))

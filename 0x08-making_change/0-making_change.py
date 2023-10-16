#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): List of coin denominations.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total. Returns -1 if impossible.
    """
    if total < 0:
        return 0
    if total == 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

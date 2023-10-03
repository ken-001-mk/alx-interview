#!/usr/bin/python3
"""Prime Game """

def isWinner(x, nums):
    """determine who the winner of each game is"""
    if x <= 0 or not nums:
        return None
    if x != len(nums):
        return None
    
    maria = 0
    ben = 0

    n = [1 for i in range(sorted(nums)[-1] + 1)]
    n[0], n[1] = 0, 0
    for i in range(2, len(n)):
        if n[i] == 1:
            for j in range(i, len(n), i):
                n[j] = 0
            
        
    for i in range(len(nums)):
        count = 0
        for j in range(2, nums[i] + 1):
            if n[j] == 1:
                count += 1
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
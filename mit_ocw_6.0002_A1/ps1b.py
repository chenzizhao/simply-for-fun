###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # constraint: total weight = 99
    # objective: minimize num of eggs
    # difference from lecture sample: can have multiple eggs with the same weight
    egg_weights = sorted(egg_weights, reverse = True)
    if target_weight <= 0:
        return float("inf") # base case 1: stop when have negative target_weight, return INF because this can never be our solution
    elif egg_weights == [1]:
        return int(target_weight/1) # base case 2: if only available weight is 1, use as many 1s as needed
    try:
        return memo[target_weight] # check if in memo
    except KeyError:
        curr_weight = egg_weights[0]
        num_with = 1 + dp_make_weight(egg_weights, target_weight - curr_weight, memo)
        num_without = dp_make_weight(filter(lambda x: x!= curr_weight, egg_weights), target_weight, memo)
        memo[target_weight] = min(num_with, num_without)
        return memo[target_weight]

        

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 20)
    n = 99
    print(f"Egg weights = {egg_weights}")
    print(f"n = {n}")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
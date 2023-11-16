from itertools import combinations

def sum_of_power(nums):
    MOD = 10**9 + 7
    n = len(nums)
    total_power = 0

    # Iterate through all possible combinations of heroes
    for r in range(1, n + 1):
        for combo in combinations(nums, r):
            print(combo)
            max_val = max(combo)
            min_val = min(combo)
            total_power = (total_power + max_val**2 * min_val) % MOD

    return total_power

# Example usage:
hero_strengths = [2, 1, 4,5]
result = sum_of_power(hero_strengths)
print(result)

def longest_square_streak(nums):
    nums_set = set(nums)
    max_streak_length = -1

    for num in nums:
        current_streak_length = 1
        current_num = num

        while current_num * current_num in nums_set:
            current_num = current_num * current_num
            current_streak_length += 1

        max_streak_length = max(max_streak_length, current_streak_length)

    return max_streak_length if max_streak_length >= 2 else -1

# Example usage:
nums = [4, 3, 6, 16, 8, 2]
result = longest_square_streak(nums)
print(result)

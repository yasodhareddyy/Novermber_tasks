def beauty_of_subarrays(nums, k, x):
    beauty_values = []

    for i in range(len(nums) - k + 1):
        subarray = nums[i:i+k]
        subarray.sort()

        beauty = 0
        if x > 0 and len([num for num in subarray if num < 0]) >= x:
            beauty = subarray[x - 1]

        beauty_values.append(beauty)

    return beauty_values

# Example usage
nums = [1, -1, -3, -2, 3]
k = 3
x=2
# When x = 2
result = beauty_of_subarrays(nums, k, x)
print(result)




